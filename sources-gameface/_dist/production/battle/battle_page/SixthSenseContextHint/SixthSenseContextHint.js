(() => {
  var u,
    e = {
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
      3733: (u, e, A) => {
        "use strict";
        var E = {};
        (A.r(E), A.d(E, { mouse: () => s, onResize: () => m }));
        var t = {};
        (A.r(t),
          A.d(t, {
            events: () => E,
            getMouseGlobalPosition: () => c,
            getSize: () => d,
            graphicsQuality: () => g,
          }));
        var F = {};
        (A.r(F), A.d(F, { getBgUrl: () => h, getTextureUrl: () => _ }));
        var D = {};
        (A.r(D),
          A.d(D, {
            addModelObserver: () => O,
            addPreloadTexture: () => H,
            children: () => F,
            displayStatus: () => x,
            displayStatusIs: () => Q,
            events: () => f,
            extraSize: () => Z,
            forceTriggerMouseMove: () => Y,
            freezeTextureBeforeResize: () => N,
            getBrowserTexturePath: () => y,
            getDisplayStatus: () => q,
            getScale: () => j,
            getSize: () => W,
            getViewGlobalPosition: () => P,
            isClientAccessible: () => U,
            isEventHandled: () => K,
            isFocused: () => k,
            pxToRem: () => X,
            remToPx: () => $,
            resize: () => I,
            sendEvent: () => M,
            setAnimateWindow: () => z,
            setEventHandled: () => V,
            setInputPaddingsRem: () => T,
            setSidePaddingsRem: () => G,
            whenTutorialReady: () => J,
          }));
        var r = A(6179),
          a = A.n(r),
          n = A(493),
          B = A.n(n);
        const i = (u, e, A) =>
          e.extraLargeHeight ||
          e.largeHeight ||
          e.mediumHeight ||
          e.smallHeight ||
          e.extraSmallHeight
            ? (e.extraLargeHeight && A.extraLarge) ||
              (e.largeHeight && A.large) ||
              (e.mediumHeight && A.medium) ||
              (e.smallHeight && A.small) ||
              (e.extraSmallHeight && A.extraSmall)
              ? u
              : null
            : u;
        function C(u) {
          return (e) => (
            engine.on(u, e),
            () => {
              engine.off(u, e);
            }
          );
        }
        function l(u) {
          viewEnv.setTrackMouseOnStage(u);
        }
        const m = C("clientResized"),
          o = { down: C("mousedown"), up: C("mouseup"), move: C("mousemove") };
        const s = (function () {
          const u = { listeners: 0, enabled: !0, initialized: !1 };
          function e() {
            u.enabled && l(!1);
          }
          function A() {
            u.enabled && l(!0);
          }
          function E() {
            u.enabled
              ? u.listeners < 1
                ? ((u.initialized = !1),
                  document.body.removeEventListener("mouseenter", e),
                  document.body.removeEventListener("mouseleave", A))
                : u.initialized ||
                  ((u.initialized = !0),
                  document.body.addEventListener("mouseenter", e),
                  document.body.addEventListener("mouseleave", A))
              : l(!1);
          }
          const t = ["down", "up", "move"].reduce(
            (e, A) => (
              (e[A] = (function (e) {
                return (A) => {
                  u.listeners += 1;
                  let t = !0;
                  const F = `mouse${e}`,
                    D = o[e]((u) => A([u, "outside"]));
                  function r(u) {
                    A([u, "inside"]);
                  }
                  return (
                    window.addEventListener(F, r),
                    E(),
                    () => {
                      t &&
                        (D(), window.removeEventListener(F, r), (u.listeners -= 1), E(), (t = !1));
                    }
                  );
                };
              })(A)),
              e
            ),
            {},
          );
          return Object.assign({}, t, {
            disable() {
              ((u.enabled = !1), E());
            },
            enable() {
              ((u.enabled = !0), E());
            },
            enableOutside() {
              u.enabled && l(!0);
            },
            disableOutside() {
              u.enabled && l(!1);
            },
          });
        })();
        function d(u = "px") {
          return "rem" === u ? viewEnv.getClientSizeRem() : viewEnv.getClientSizePx();
        }
        function c(u = "px") {
          return "rem" === u
            ? viewEnv.getMouseGlobalPositionRem()
            : viewEnv.getMouseGlobalPositionPx();
        }
        const g = {
          isLow: () => 1 === viewEnv.getGraphicsQuality(),
          isHigh: () => 0 === viewEnv.getGraphicsQuality(),
          get: () => viewEnv.getGraphicsQuality(),
        };
        function _(u, e, A = 1) {
          return viewEnv.getChildTexturePath(u, e.width, e.height, A);
        }
        function h(u, e, A) {
          return `url(${_(u, e, A)})`;
        }
        const x = { showing: 0, shown: 1, hiding: 2, hidden: 3 },
          f = {
            onTextureFrozen: C("self.onTextureFrozen"),
            onTextureReady: C("self.onTextureReady"),
            onDomBuilt: C("self.onDomBuilt"),
            onLoaded: C("self.onLoaded"),
            onDisplayChanged: C("self.onShowingStatusChanged"),
            onFocusUpdated: C("self.onFocusChanged"),
            children: {
              onAdded: C("children.onAdded"),
              onLoaded: C("children.onLoaded"),
              onRemoved: C("children.onRemoved"),
              onAttached: C("children.onAttached"),
              onTextureReady: C("children.onTextureReady"),
              onRequestPosition: C("children.requestPosition"),
            },
          },
          p = ["args"];
        const v = 2,
          S = 16,
          b = 32,
          L = 64,
          w = (u, e) => {
            const A = "GFViewEventProxy";
            if (void 0 !== e) {
              const t = e.args,
                F = (function (u, e) {
                  if (null == u) return {};
                  var A,
                    E,
                    t = {},
                    F = Object.keys(u);
                  for (E = 0; E < F.length; E++) ((A = F[E]), e.indexOf(A) >= 0 || (t[A] = u[A]));
                  return t;
                })(e, p);
              return void 0 !== t
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: A, type: u }, F, {
                      arguments:
                        ((E = t),
                        Object.entries(E).map(([u, e]) => {
                          const A = "GFValueProxy";
                          switch (typeof e) {
                            case "number":
                              return { __Type: A, name: u, number: e };
                            case "boolean":
                              return { __Type: A, name: u, bool: e };
                            default:
                              return { __Type: A, name: u, string: e.toString() };
                          }
                        })),
                    }),
                  )
                : viewEnv.handleViewEvent(Object.assign({ __Type: A, type: u }, F));
            }
            return viewEnv.handleViewEvent({ __Type: A, type: u });
            var E;
          },
          M = {
            close(u) {
              w("popover" === u ? v : b);
            },
            minimize() {
              w(L);
            },
            move(u) {
              w(S, { isMouseEvent: !0, on: u });
            },
          };
        function H(u) {
          viewEnv.addPreloadTexture(u);
        }
        function T(u) {
          viewEnv.setHitAreaPaddingsRem(u, u, u, u, 15);
        }
        function y(u, e, A, E = 1) {
          return viewEnv.getWebBrowserTexturePath(u, e, A, E);
        }
        function O(u, e, A) {
          return viewEnv.addDataChangedCallback(u, e, A);
        }
        function G(u) {
          viewEnv.setHitAreaPaddingsRem(u.top, u.right, u.bottom, u.left, 15);
        }
        function W(u = "px") {
          return "rem" === u ? viewEnv.getViewSizeRem() : viewEnv.getViewSizePx();
        }
        function I(u, e, A = "px") {
          return "rem" === A ? viewEnv.resizeViewRem(u, e) : viewEnv.resizeViewPx(u, e);
        }
        function P(u = "rem") {
          const e = viewEnv.getViewGlobalPositionRem();
          return "rem" === u ? e : { x: $(e.x), y: $(e.y) };
        }
        function N() {
          viewEnv.freezeTextureBeforeResize();
        }
        function j() {
          return viewEnv.getScale();
        }
        function X(u) {
          return viewEnv.pxToRem(u);
        }
        function $(u) {
          return viewEnv.remToPx(u);
        }
        function z(u, e) {
          viewEnv.setAnimateWindow(u, e);
        }
        function k() {
          return viewEnv.isFocused();
        }
        function U() {
          return viewEnv.isClientAccessible();
        }
        function V() {
          return viewEnv.setEventHandled();
        }
        function K() {
          return viewEnv.isEventHandled();
        }
        function Y() {
          viewEnv.forceTriggerMouseMove();
        }
        function q() {
          return viewEnv.getShowingStatus();
        }
        const Q = Object.keys(x).reduce(
            (u, e) => ((u[e] = () => viewEnv.getShowingStatus() === x[e]), u),
            {},
          ),
          Z = {
            set: (u, e) => {
              viewEnv.setExtraSizeRem(u, e);
            },
            get: (u, e) => {
              viewEnv.getExtraSizeRem(u, e);
            },
          },
          J = Promise.all([
            new Promise((u) => {
              window.isDomBuilt ? u() : f.onDomBuilt(u);
            }),
            engine.whenReady,
          ]),
          uu = { view: D, client: t };
        const eu = {
          extraLarge: { weight: 4, width: 2560, height: 1440 },
          large: { weight: 3, width: 1920, height: 1080 },
          medium: { weight: 2, width: 1600, height: 900 },
          small: { weight: 1, width: 1366, height: 768 },
          extraSmall: { weight: 0, width: 1024, height: 768 },
        };
        var Au;
        function Eu(u, e, A) {
          const E = (function (u, e) {
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
            })(u, A),
            t = (function (u, e) {
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
            })(e, A),
            F = Math.min(E, t);
          return {
            extraLarge: F === A.extraLarge.weight,
            large: F === A.large.weight,
            medium: F === A.medium.weight,
            small: F === A.small.weight,
            extraSmall: F === A.extraSmall.weight,
            extraLargeWidth: E === A.extraLarge.weight,
            largeWidth: E === A.large.weight,
            mediumWidth: E === A.medium.weight,
            smallWidth: E === A.small.weight,
            extraSmallWidth: E === A.extraSmall.weight,
            extraLargeHeight: t === A.extraLarge.weight,
            largeHeight: t === A.large.weight,
            mediumHeight: t === A.medium.weight,
            smallHeight: t === A.small.weight,
            extraSmallHeight: t === A.extraSmall.weight,
          };
        }
        !(function (u) {
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
        })(Au || (Au = {}));
        const tu = uu.client.getSize("rem"),
          Fu = tu.width,
          Du = tu.height,
          ru = Object.assign({ width: Fu, height: Du }, Eu(Fu, Du, eu)),
          au = (0, r.createContext)(ru),
          nu = ["children"];
        const Bu = (u) => {
          let e = u.children,
            A = (function (u, e) {
              if (null == u) return {};
              var A,
                E,
                t = {},
                F = Object.keys(u);
              for (E = 0; E < F.length; E++) ((A = F[E]), e.indexOf(A) >= 0 || (t[A] = u[A]));
              return t;
            })(u, nu);
          const E = (0, r.useContext)(au),
            t = E.extraLarge,
            F = E.large,
            D = E.medium,
            a = E.small,
            n = E.extraSmall,
            B = E.extraLargeWidth,
            C = E.largeWidth,
            l = E.mediumWidth,
            m = E.smallWidth,
            o = E.extraSmallWidth,
            s = E.extraLargeHeight,
            d = E.largeHeight,
            c = E.mediumHeight,
            g = E.smallHeight,
            _ = E.extraSmallHeight,
            h = { extraLarge: s, large: d, medium: c, small: g, extraSmall: _ };
          if (A.extraLarge || A.large || A.medium || A.small || A.extraSmall) {
            if (A.extraLarge && t) return e;
            if (A.large && F) return e;
            if (A.medium && D) return e;
            if (A.small && a) return e;
            if (A.extraSmall && n) return e;
          } else {
            if (A.extraLargeWidth && B) return i(e, A, h);
            if (A.largeWidth && C) return i(e, A, h);
            if (A.mediumWidth && l) return i(e, A, h);
            if (A.smallWidth && m) return i(e, A, h);
            if (A.extraSmallWidth && o) return i(e, A, h);
            if (!(
              A.extraLargeWidth ||
              A.largeWidth ||
              A.mediumWidth ||
              A.smallWidth ||
              A.extraSmallWidth
            )) {
              if (A.extraLargeHeight && s) return e;
              if (A.largeHeight && d) return e;
              if (A.mediumHeight && c) return e;
              if (A.smallHeight && g) return e;
              if (A.extraSmallHeight && _) return e;
            }
          }
          return null;
        };
        Bu.defaultProps = {
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
        (0, r.memo)(Bu);
        const iu = (u) => {
            const e = (0, r.useRef)(!1);
            e.current || (u(), (e.current = !0));
          },
          Cu = (0, r.memo)(({ children: u }) => {
            const e = (0, r.useContext)(au),
              A = (0, r.useState)(e),
              E = A[0],
              t = A[1],
              F = (0, r.useCallback)((u, e) => {
                const A = uu.view.pxToRem(u),
                  E = uu.view.pxToRem(e);
                t(Object.assign({ width: A, height: E }, Eu(A, E, eu)));
              }, []);
            (iu(() => {
              engine.on("clientResized", F);
            }),
              (0, r.useEffect)(() => () => engine.off("clientResized", F), [F]));
            const D = (0, r.useMemo)(() => Object.assign({}, E), [E]);
            return a().createElement(au.Provider, { value: D }, u);
          });
        var lu = A(6483),
          mu = A.n(lu),
          ou = A(926),
          su = A.n(ou);
        let du, cu, gu;
        (!(function (u) {
          ((u[(u.ExtraSmall = eu.extraSmall.width)] = "ExtraSmall"),
            (u[(u.Small = eu.small.width)] = "Small"),
            (u[(u.Medium = eu.medium.width)] = "Medium"),
            (u[(u.Large = eu.large.width)] = "Large"),
            (u[(u.ExtraLarge = eu.extraLarge.width)] = "ExtraLarge"));
        })(du || (du = {})),
          (function (u) {
            ((u[(u.ExtraSmall = eu.extraSmall.width)] = "ExtraSmall"),
              (u[(u.Small = eu.small.width)] = "Small"),
              (u[(u.Medium = eu.medium.width)] = "Medium"),
              (u[(u.Large = eu.large.width)] = "Large"),
              (u[(u.ExtraLarge = eu.extraLarge.width)] = "ExtraLarge"));
          })(cu || (cu = {})),
          (function (u) {
            ((u[(u.ExtraSmall = eu.extraSmall.height)] = "ExtraSmall"),
              (u[(u.Small = eu.small.height)] = "Small"),
              (u[(u.Medium = eu.medium.height)] = "Medium"),
              (u[(u.Large = eu.large.height)] = "Large"),
              (u[(u.ExtraLarge = eu.extraLarge.height)] = "ExtraLarge"));
          })(gu || (gu = {})));
        const _u = () => {
            const u = (0, r.useContext)(au),
              e = u.width,
              A = u.height,
              E = ((u) => {
                switch (!0) {
                  case u.extraLarge:
                    return du.ExtraLarge;
                  case u.large:
                    return du.Large;
                  case u.medium:
                    return du.Medium;
                  case u.small:
                    return du.Small;
                  case u.extraSmall:
                    return du.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), du.ExtraSmall);
                }
              })(u),
              t = ((u) => {
                switch (!0) {
                  case u.extraLargeWidth:
                    return cu.ExtraLarge;
                  case u.largeWidth:
                    return cu.Large;
                  case u.mediumWidth:
                    return cu.Medium;
                  case u.smallWidth:
                    return cu.Small;
                  case u.extraSmallWidth:
                    return cu.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), cu.ExtraSmall);
                }
              })(u),
              F = ((u) => {
                switch (!0) {
                  case u.extraLargeHeight:
                    return gu.ExtraLarge;
                  case u.largeHeight:
                    return gu.Large;
                  case u.mediumHeight:
                    return gu.Medium;
                  case u.smallHeight:
                    return gu.Small;
                  case u.extraSmallHeight:
                    return gu.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), gu.ExtraSmall);
                }
              })(u);
            return {
              mediaSize: E,
              mediaWidth: t,
              mediaHeight: F,
              remScreenWidth: e,
              remScreenHeight: A,
            };
          },
          hu = ["children", "className"];
        function xu() {
          return (
            (xu =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var A = arguments[e];
                  for (var E in A) Object.prototype.hasOwnProperty.call(A, E) && (u[E] = A[E]);
                }
                return u;
              }),
            xu.apply(this, arguments)
          );
        }
        const fu = {
            [cu.ExtraSmall]: "",
            [cu.Small]: su().SMALL_WIDTH,
            [cu.Medium]: `${su().SMALL_WIDTH} ${su().MEDIUM_WIDTH}`,
            [cu.Large]: `${su().SMALL_WIDTH} ${su().MEDIUM_WIDTH} ${su().LARGE_WIDTH}`,
            [cu.ExtraLarge]: `${su().SMALL_WIDTH} ${su().MEDIUM_WIDTH} ${su().LARGE_WIDTH} ${su().EXTRA_LARGE_WIDTH}`,
          },
          pu = {
            [gu.ExtraSmall]: "",
            [gu.Small]: su().SMALL_HEIGHT,
            [gu.Medium]: `${su().SMALL_HEIGHT} ${su().MEDIUM_HEIGHT}`,
            [gu.Large]: `${su().SMALL_HEIGHT} ${su().MEDIUM_HEIGHT} ${su().LARGE_HEIGHT}`,
            [gu.ExtraLarge]: `${su().SMALL_HEIGHT} ${su().MEDIUM_HEIGHT} ${su().LARGE_HEIGHT} ${su().EXTRA_LARGE_HEIGHT}`,
          },
          vu = {
            [du.ExtraSmall]: "",
            [du.Small]: su().SMALL,
            [du.Medium]: `${su().SMALL} ${su().MEDIUM}`,
            [du.Large]: `${su().SMALL} ${su().MEDIUM} ${su().LARGE}`,
            [du.ExtraLarge]: `${su().SMALL} ${su().MEDIUM} ${su().LARGE} ${su().EXTRA_LARGE}`,
          },
          Su = (u) => {
            let e = u.children,
              A = u.className,
              E = (function (u, e) {
                if (null == u) return {};
                var A,
                  E,
                  t = {},
                  F = Object.keys(u);
                for (E = 0; E < F.length; E++) ((A = F[E]), e.indexOf(A) >= 0 || (t[A] = u[A]));
                return t;
              })(u, hu);
            const t = _u(),
              F = t.mediaWidth,
              D = t.mediaHeight,
              r = t.mediaSize;
            return a().createElement("div", xu({ className: mu()(A, fu[F], pu[D], vu[r]) }, E), e);
          },
          bu = ["children"];
        const Lu = (u) => {
          let e = u.children,
            A = (function (u, e) {
              if (null == u) return {};
              var A,
                E,
                t = {},
                F = Object.keys(u);
              for (E = 0; E < F.length; E++) ((A = F[E]), e.indexOf(A) >= 0 || (t[A] = u[A]));
              return t;
            })(u, bu);
          return a().createElement(Cu, null, a().createElement(Su, A, e));
        };
        function wu() {
          return !1;
        }
        console.log;
        var Mu = A(9174);
        function Hu(u, e) {
          var A = ("undefined" != typeof Symbol && u[Symbol.iterator]) || u["@@iterator"];
          if (A) return (A = A.call(u)).next.bind(A);
          if (
            Array.isArray(u) ||
            (A = (function (u, e) {
              if (!u) return;
              if ("string" == typeof u) return Tu(u, e);
              var A = Object.prototype.toString.call(u).slice(8, -1);
              "Object" === A && u.constructor && (A = u.constructor.name);
              if ("Map" === A || "Set" === A) return Array.from(u);
              if ("Arguments" === A || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(A))
                return Tu(u, e);
            })(u)) ||
            (e && u && "number" == typeof u.length)
          ) {
            A && (u = A);
            var E = 0;
            return function () {
              return E >= u.length ? { done: !0 } : { done: !1, value: u[E++] };
            };
          }
          throw new TypeError(
            "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.",
          );
        }
        function Tu(u, e) {
          (null == e || e > u.length) && (e = u.length);
          for (var A = 0, E = new Array(e); A < e; A++) E[A] = u[A];
          return E;
        }
        const Ru = (u) => (0 === u ? window : window.subViews.get(u));
        const yu = ((u, e) => {
            const A = (0, r.createContext)({});
            return [
              function ({ mode: E = "real", options: t, children: F, mocks: D }) {
                const n = (0, r.useRef)([]),
                  B = (A, E, t) => {
                    var F;
                    const D = (function ({
                        initializer: u = !0,
                        rootId: e = 0,
                        getRoot: A = Ru,
                        context: E = "model",
                      } = {}) {
                        const t = new Map();
                        function F(u, e = 0) {
                          viewEnv.removeDataChangedCallback(u, e)
                            ? t.delete(u)
                            : console.error("Can't remove callback by id:", u);
                        }
                        engine.whenReady.then(() => {
                          engine.on("viewEnv.onDataChanged", (u, e, A) => {
                            A.forEach((e) => {
                              const A = t.get(e);
                              void 0 !== A && A(u);
                            });
                          });
                        });
                        const D = (u) => {
                          const t = A(e),
                            F = E.split(".").reduce((u, e) => u[e], t);
                          return "string" != typeof u || 0 === u.length
                            ? F
                            : u.split(".").reduce((u, e) => {
                                const A = u[e];
                                return "function" == typeof A ? A.bind(u) : A;
                              }, F);
                        };
                        return {
                          subscribe: (A, F) => {
                            const r = "string" == typeof F ? `${E}.${F}` : E,
                              a = uu.view.addModelObserver(r, e, !0);
                            return (t.set(a, A), u && A(D(F)), a);
                          },
                          readByPath: D,
                          createCallback: (u, e) => {
                            const A = D(e);
                            return (...e) => {
                              A(u(...e));
                            };
                          },
                          createCallbackNoArgs: (u) => {
                            const e = D(u);
                            return () => {
                              e();
                            };
                          },
                          dispose: function () {
                            for (var u, A = Hu(t.keys()); !(u = A()).done;) F(u.value, e);
                          },
                          unsubscribe: F,
                        };
                      })(E),
                      r =
                        "real" === A
                          ? D
                          : Object.assign({}, D, {
                              readByPath:
                                null != (F = null == t ? void 0 : t.getter) ? F : () => {},
                            }),
                      a = (u) =>
                        "mocks" === A ? (null == t ? void 0 : t.getter(u)) : r.readByPath(u),
                      B = (u) => n.current.push(u),
                      i = u({
                        mode: A,
                        readByPath: a,
                        externalModel: r,
                        observableModel: {
                          array: (u, e) => {
                            const E = null != e ? e : a(u),
                              t = Mu.LO.box(E, { equals: wu });
                            return (
                              "real" === A &&
                                r.subscribe(
                                  (0, Mu.aD)((u) => t.set(u)),
                                  u,
                                ),
                              t
                            );
                          },
                          object: (u, e) => {
                            const E = null != e ? e : a(u),
                              t = Mu.LO.box(E, { equals: wu });
                            return (
                              "real" === A &&
                                r.subscribe(
                                  (0, Mu.aD)((u) => t.set(u)),
                                  u,
                                ),
                              t
                            );
                          },
                          primitives: (u, e) => {
                            const E = a(e);
                            if (Array.isArray(u)) {
                              const t = u.reduce((u, e) => ((u[e] = Mu.LO.box(E[e], {})), u), {});
                              return (
                                "real" === A &&
                                  r.subscribe(
                                    (0, Mu.aD)((e) => {
                                      u.forEach((u) => {
                                        t[u].set(e[u]);
                                      });
                                    }),
                                    e,
                                  ),
                                t
                              );
                            }
                            {
                              const t = u,
                                F = Object.entries(t),
                                D = F.reduce((u, [e, A]) => ((u[A] = Mu.LO.box(E[e], {})), u), {});
                              return (
                                "real" === A &&
                                  r.subscribe(
                                    (0, Mu.aD)((u) => {
                                      F.forEach(([e, A]) => {
                                        D[A].set(u[e]);
                                      });
                                    }),
                                    e,
                                  ),
                                D
                              );
                            }
                          },
                        },
                        cleanup: B,
                      }),
                      C = { mode: A, model: i, externalModel: r, cleanup: B };
                    return {
                      model: i,
                      controls: "mocks" === A && t ? t.controls(C) : e(C),
                      externalModel: r,
                      mode: A,
                    };
                  },
                  i = (0, r.useRef)(!1),
                  C = (0, r.useState)(E),
                  l = C[0],
                  m = C[1],
                  o = (0, r.useState)(() => B(E, t, D)),
                  s = o[0],
                  d = o[1];
                return (
                  (0, r.useEffect)(() => {
                    i.current ? d(B(l, t, D)) : (i.current = !0);
                  }, [D, l, t]),
                  (0, r.useEffect)(() => {
                    m(E);
                  }, [E]),
                  (0, r.useEffect)(
                    () => () => {
                      (s.externalModel.dispose(), n.current.forEach((u) => u()));
                    },
                    [s],
                  ),
                  a().createElement(A.Provider, { value: s }, F)
                );
              },
              () => (0, r.useContext)(A),
            ];
          })(
            ({ observableModel: u }) => {
              const e = Object.assign({ root: u.object() }, u.primitives(["isVisible"]));
              return Object.assign({}, e);
            },
            ({ externalModel: u }) => ({ onHintClosed: u.createCallbackNoArgs("onHintClosed") }),
          ),
          Ou = yu[0],
          Gu = yu[1];
        var Wu = A(9887),
          Iu = A.n(Wu);
        const Pu = ["xl", "lg", "md", "sm", "xs"],
          Nu = (u) => u.includes("_") && ((u) => Pu.includes(u))(u.split("_").at(-1)),
          ju = [du.ExtraLarge, du.Large, du.Medium, du.Small, du.ExtraSmall],
          Xu = (u, e) =>
            Object.keys(u).reduce((A, E) => {
              if (E in A) return A;
              if (Nu(E)) {
                const t = E.split("_").slice(0, -1).join("_");
                if (t in A) return A;
                const F = ju.indexOf(e),
                  D = (-1 !== F ? Pu.slice(F) : [])
                    .map((u) => t + "_" + u)
                    .find((e) => void 0 !== u[e]),
                  r = D ? u[D] : void 0;
                return ((A[t] = void 0 !== r ? r : u[t]), A);
              }
              const t = u[E];
              return (
                void 0 === t ||
                  ((u, e) => Pu.some((A) => void 0 !== e[`${u}_${A}`]))(E, u) ||
                  (A[E] = t),
                A
              );
            }, {}),
          $u = (u, e = Xu) => {
            const A = (
              (u, e = Xu) =>
              (A) => {
                const E = _u().mediaSize,
                  t = (0, r.useMemo)(() => e(A, E), [A, E]);
                return a().createElement(u, t);
              }
            )(u, e);
            return a().memo((e) =>
              Object.keys(e).some((u) => Nu(u) && void 0 !== e[u])
                ? a().createElement(A, e)
                : a().createElement(u, e),
            );
          },
          zu = {
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
          ku = [
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
        function Uu() {
          return (
            (Uu =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var A = arguments[e];
                  for (var E in A) Object.prototype.hasOwnProperty.call(A, E) && (u[E] = A[E]);
                }
                return u;
              }),
            Uu.apply(this, arguments)
          );
        }
        Object.keys(Iu());
        const Vu = {
            XL: { mt: zu.mt__XL, mr: zu.mr__XL, mb: zu.mb__XL, ml: zu.ml__XL },
            LG: { mt: zu.mt__LG, mr: zu.mr__LG, mb: zu.mb__LG, ml: zu.ml__LG },
            MDp: { mt: zu.mt__MDp, mr: zu.mr__MDp, mb: zu.mb__MDp, ml: zu.ml__MDp },
            MD: { mt: zu.mt__MD, mr: zu.mr__MD, mb: zu.mb__MD, ml: zu.ml__MD },
            SMp: { mt: zu.mt__SMp, mr: zu.mr__SMp, mb: zu.mb__SMp, ml: zu.ml__SMp },
            SM: { mt: zu.mt__SM, mr: zu.mr__SM, mb: zu.mb__SM, ml: zu.ml__SM },
            XS: { mt: zu.mt__XS, mr: zu.mr__XS, mb: zu.mb__XS, ml: zu.ml__XS },
          },
          Ku = (Object.keys(Vu), ["mt", "mr", "mb", "ml"]),
          Yu = { mt: "marginTop", mr: "marginRight", mb: "marginBottom", ml: "marginLeft" },
          qu = $u((u) => {
            let e = u.className,
              A = u.width,
              E = u.height,
              t = u.m,
              F = u.mt,
              D = void 0 === F ? t : F,
              n = u.mr,
              B = void 0 === n ? t : n,
              i = u.mb,
              C = void 0 === i ? t : i,
              l = u.ml,
              m = void 0 === l ? t : l,
              o = u.column,
              s = u.row,
              d = u.flexDirection,
              c = void 0 === d ? (o ? "column" : s && "row") || void 0 : d,
              g = u.flexStart,
              _ = u.center,
              h = u.flexEnd,
              x = u.spaceBetween,
              f = u.spaceAround,
              p = u.justifyContent,
              v =
                void 0 === p
                  ? (g ? "flex-start" : _ && "center") ||
                    (h && "flex-end") ||
                    (x && "space-between") ||
                    (f && "space-around") ||
                    void 0
                  : p,
              S = u.alignItems,
              b =
                void 0 === S
                  ? (g ? "flex-start" : _ && "center") || (h && "flex-end") || void 0
                  : S,
              L = u.alignSelf,
              w = u.wrap,
              M = u.flexWrap,
              H = void 0 === M ? (w ? "wrap" : void 0) : M,
              T = u.grow,
              R = u.shrink,
              y = u.flex,
              O = void 0 === y ? (T || R ? `${T ? 1 : 0} ${R ? 1 : 0} auto` : void 0) : y,
              G = u.style,
              W = u.children,
              I = (function (u, e) {
                if (null == u) return {};
                var A,
                  E,
                  t = {},
                  F = Object.keys(u);
                for (E = 0; E < F.length; E++) ((A = F[E]), e.indexOf(A) >= 0 || (t[A] = u[A]));
                return t;
              })(u, ku);
            const P = (0, r.useMemo)(() => {
                const u = { mt: D, mr: B, mb: C, ml: m },
                  e = ((u) =>
                    Ku.reduce((e, A) => {
                      const E = u[A];
                      return E && "number" != typeof E ? e.concat(Vu[!0 === E ? "MD" : E][A]) : e;
                    }, []))(u),
                  t = ((u) =>
                    Ku.reduce((e, A) => {
                      const E = u[A];
                      return ("number" == typeof E && (e[Yu[A]] = E + "rem"), e);
                    }, {}))(u);
                return {
                  computedStyle: Object.assign({}, G, t, {
                    width: void 0 !== A && "number" == typeof A ? A + "rem" : A,
                    height: void 0 !== E && "number" == typeof E ? E + "rem" : E,
                    flex: O,
                    alignSelf: L,
                    display: c || b ? "flex" : void 0,
                    flexDirection: c,
                    flexWrap: H,
                    justifyContent: v,
                    alignItems: b,
                  }),
                  computedClassNames: e,
                };
              }, [A, E, D, B, C, m, G, O, L, c, H, v, b]),
              N = P.computedStyle,
              j = P.computedClassNames;
            return a().createElement(
              "div",
              Uu({ className: mu()(zu.base, ...j, e), style: N }, I),
              W,
            );
          });
        let Qu;
        !(function (u) {
          ((u[(u.left = 0)] = "left"), (u[(u.right = 1)] = "right"));
        })(Qu || (Qu = {}));
        const Zu = (u, e, A) => {
            if (A % 2) {
              const A = u.pop();
              return [...u, A + e];
            }
            return [...u, e];
          },
          Ju = (u, e, A) => {
            if (0 === A) return [e];
            if (A % 2) return [...u, " " === e ? " " : e];
            {
              const A = u.pop();
              return [...u, A + e];
            }
          },
          ue = (u, e, A = Qu.left) => u.split(e).reduce(A === Qu.left ? Zu : Ju, []),
          ee = (() => {
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
          Ae = ["zh_cn", "zh_sg", "zh_tw"],
          Ee = (u, e = Qu.left) => {
            const A = R.strings.settings.LANGUAGE_CODE().toLowerCase();
            return Ae.includes(A)
              ? ee(u)
              : ((u, e = Qu.left) => {
                  let A = [];
                  const E =
                      /(?<=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])(\x2D)(?=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])/gu,
                    t = u.replace(/&nbsp;/g, " ");
                  return (ue(t, /( )/, e).forEach((u) => (A = A.concat(ue(u, E, Qu.left)))), A);
                })(u, e);
          },
          te = "FormatText_base_d0",
          Fe = ({ binding: u, text: e = "", classMix: A, alignment: E = Qu.left }) =>
            null === e
              ? (console.error("FormatText was supplied with 'null'"), null)
              : a().createElement(
                  r.Fragment,
                  null,
                  e.split("\n").map((e, t) =>
                    a().createElement(
                      "div",
                      { className: mu()(te, A), key: `${e}-${t}` },
                      ((u, e, A) =>
                        u
                          .split(/%\((.*?)\)(?:[sd])?/g)
                          .map((u) => (A && u in A ? A[u] : Ee(u, e))))(e, E, u).map((u, e) =>
                        a().createElement(r.Fragment, { key: `${e}-${u}` }, u),
                      ),
                    ),
                  ),
                );
        var De = A(3532),
          re = A.n(De);
        const ae = {
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
          ne = [
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
        function Be() {
          return (
            (Be =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var A = arguments[e];
                  for (var E in A) Object.prototype.hasOwnProperty.call(A, E) && (u[E] = A[E]);
                }
                return u;
              }),
            Be.apply(this, arguments)
          );
        }
        Object.keys(Iu());
        const ie = Object.keys(re()),
          Ce = { mt: "MD", mr: "SM", mb: "SM", ml: "SM" },
          le = { mt: "SM", mr: "XS", mb: "XS", ml: "XS" },
          me = { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          oe = {
            XL: { mt: "XL", mr: "XL", mb: "XL", ml: "XL" },
            LG: { mt: "LG", mr: "LG", mb: "LG", ml: "LG" },
            MDp: { mt: "MDp", mr: "MDp", mb: "MDp", ml: "MDp" },
            MD: { mt: "MD", mr: "MD", mb: "MD", ml: "MD" },
            SMp: { mt: "SMp", mr: "SMp", mb: "SMp", ml: "SMp" },
            SM: { mt: "SM", mr: "SM", mb: "SM", ml: "SM" },
            XS: { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          },
          se =
            (Object.keys(oe),
            {
              "heading-H144": { mt: "XL", mr: "LG", mb: "LG", ml: "LG" },
              "heading-H73": { mt: "LG", mr: "MD", mb: "MD", ml: "MD" },
              "heading-H56": Ce,
              "heading-H36": Ce,
              "heading-H28": le,
              "heading-H24": le,
              "heading-H24R": le,
              "heading-H22": le,
              "heading-H20R": le,
              "heading-H18": le,
              "heading-H15": me,
              "heading-H14": me,
              "paragraph-P24": le,
              "paragraph-P18": le,
              "paragraph-P16": le,
              "paragraph-P14": me,
              "paragraph-P12": me,
              "paragraph-P10": me,
            }),
          de =
            (Object.keys(se),
            (u) =>
              u
                ? ((u) => ie.includes(u))(u)
                  ? { colorClassName: ae[u] }
                  : { colorStyle: { color: u } }
                : {}),
          ce = $u((u) => {
            let e = u.text,
              A = u.variant,
              E = u.className,
              t = u.color,
              F = u.m,
              D = u.mt,
              n = void 0 === D ? F : D,
              B = u.mr,
              i = void 0 === B ? F : B,
              C = u.mb,
              l = void 0 === C ? F : C,
              m = u.ml,
              o = void 0 === m ? F : m,
              s = u.style,
              d = u.format,
              c = (function (u, e) {
                if (null == u) return {};
                var A,
                  E,
                  t = {},
                  F = Object.keys(u);
                for (E = 0; E < F.length; E++) ((A = F[E]), e.indexOf(A) >= 0 || (t[A] = u[A]));
                return t;
              })(u, ne);
            const g = (0, r.useMemo)(() => {
                const u = de(t),
                  e = u.colorClassName,
                  A = u.colorStyle,
                  E = void 0 === A ? {} : A;
                return { computedStyle: Object.assign({}, s, E), colorClassName: e };
              }, [s, t]),
              _ = g.computedStyle,
              h = g.colorClassName;
            return a().createElement(
              qu,
              Be(
                {
                  className: mu()(ae.base, A && ae[A], h, E),
                  style: _,
                  mt: !0 === n ? se[A || "paragraph-P16"].mt : n,
                  mr: !0 === i ? se[A || "paragraph-P16"].mr : i,
                  mb: !0 === l ? se[A || "paragraph-P16"].mb : l,
                  ml: !0 === o ? se[A || "paragraph-P16"].ml : o,
                },
                c,
              ),
              void 0 !== d ? a().createElement(Fe, Be({}, d, { text: e })) : e,
            );
          });
        var ge = A(3403);
        const _e = "App_base_a6",
          he = "App_shineLineAnimation_d6",
          xe = "App_lightRedAnimation_23",
          fe = "App_text_03",
          pe = "App_textClosing_0f";
        var ve;
        !(function (u) {
          ((u.Idle = "idle"), (u.Visible = "visible"), (u.Closing = "closing"));
        })(ve || (ve = {}));
        const Se = (0, ge.Pi)(() => {
          const u = Gu(),
            e = u.model,
            A = u.controls,
            E = (0, r.useState)(ve.Idle),
            t = E[0],
            F = E[1],
            D = e.isVisible.get();
          return (
            (0, r.useEffect)(() => {
              if (!D) return;
              F(ve.Visible);
              const u = setTimeout(() => {
                F(ve.Closing);
              }, 2e3);
              return () => clearTimeout(u);
            }, [D]),
            (0, r.useEffect)(() => {
              if (t !== ve.Closing) return;
              const u = setTimeout(() => {
                (F(ve.Idle), A.onHintClosed());
              }, 200);
              return () => clearTimeout(u);
            }, [t]),
            t === ve.Idle
              ? null
              : a().createElement(
                  "div",
                  { className: _e },
                  a().createElement("div", { className: he }),
                  a().createElement("div", { className: xe }),
                  a().createElement(ce, {
                    text: R.strings.battle_hints.sixthSenseContextHint(),
                    className: mu()(fe, { [pe]: t === ve.Closing }),
                  }),
                )
          );
        });
        engine.whenReady.then(() => {
          B().render(
            a().createElement(Ou, null, a().createElement(Lu, null, a().createElement(Se, null))),
            document.getElementById("root"),
          );
        });
      },
    },
    A = {};
  function E(u) {
    var t = A[u];
    if (void 0 !== t) return t.exports;
    var F = (A[u] = { exports: {} });
    return (e[u](F, F.exports, E), F.exports);
  }
  ((E.m = e),
    (u = []),
    (E.O = (e, A, t, F) => {
      if (!A) {
        var D = 1 / 0;
        for (B = 0; B < u.length; B++) {
          for (var [A, t, F] = u[B], r = !0, a = 0; a < A.length; a++)
            (!1 & F || D >= F) && Object.keys(E.O).every((u) => E.O[u](A[a]))
              ? A.splice(a--, 1)
              : ((r = !1), F < D && (D = F));
          if (r) {
            u.splice(B--, 1);
            var n = t();
            void 0 !== n && (e = n);
          }
        }
        return e;
      }
      F = F || 0;
      for (var B = u.length; B > 0 && u[B - 1][2] > F; B--) u[B] = u[B - 1];
      u[B] = [A, t, F];
    }),
    (E.n = (u) => {
      var e = u && u.__esModule ? () => u.default : () => u;
      return (E.d(e, { a: e }), e);
    }),
    (E.d = (u, e) => {
      for (var A in e)
        E.o(e, A) && !E.o(u, A) && Object.defineProperty(u, A, { enumerable: !0, get: e[A] });
    }),
    (E.g = (function () {
      if ("object" == typeof globalThis) return globalThis;
      try {
        return this || new Function("return this")();
      } catch (u) {
        if ("object" == typeof window) return window;
      }
    })()),
    (E.o = (u, e) => Object.prototype.hasOwnProperty.call(u, e)),
    (E.r = (u) => {
      ("undefined" != typeof Symbol &&
        Symbol.toStringTag &&
        Object.defineProperty(u, Symbol.toStringTag, { value: "Module" }),
        Object.defineProperty(u, "__esModule", { value: !0 }));
    }),
    (E.j = 334),
    (() => {
      var u = { 334: 0 };
      E.O.j = (e) => 0 === u[e];
      var e = (e, A) => {
          var t,
            F,
            [D, r, a] = A,
            n = 0;
          if (D.some((e) => 0 !== u[e])) {
            for (t in r) E.o(r, t) && (E.m[t] = r[t]);
            if (a) var B = a(E);
          }
          for (e && e(A); n < D.length; n++)
            ((F = D[n]), E.o(u, F) && u[F] && u[F][0](), (u[F] = 0));
          return E.O(B);
        },
        A = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (A.forEach(e.bind(null, 0)), (A.push = e.bind(null, A.push.bind(A))));
    })());
  var t = E.O(void 0, [532], () => E(3733));
  t = E.O(t);
})();
