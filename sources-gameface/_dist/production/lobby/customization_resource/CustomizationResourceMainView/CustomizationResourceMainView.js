(() => {
  var __webpack_modules__ = {
      380: (e) => {
        "use strict";
        function t(e) {
          return getComputedStyle(e);
        }
        function u(e, t) {
          for (var u in t) {
            var n = t[u];
            ("number" == typeof n && (n += "px"), (e.style[u] = n));
          }
          return e;
        }
        function n(e) {
          var t = document.createElement("div");
          return ((t.className = e), t);
        }
        var r =
          "undefined" != typeof Element &&
          (Element.prototype.matches ||
            Element.prototype.webkitMatchesSelector ||
            Element.prototype.mozMatchesSelector ||
            Element.prototype.msMatchesSelector);
        function o(e, t) {
          if (!r) throw new Error("No element matching method supported");
          return r.call(e, t);
        }
        function a(e) {
          e.remove ? e.remove() : e.parentNode && e.parentNode.removeChild(e);
        }
        function i(e, t) {
          return Array.prototype.filter.call(e.children, function (e) {
            return o(e, t);
          });
        }
        var l = "ps",
          s = {
            thumb: function (e) {
              return "ps__thumb-" + e;
            },
            rail: function (e) {
              return "ps__rail-" + e;
            },
            buttonStart: function (e) {
              return "ps__button-start-" + e;
            },
            track: function (e) {
              return "ps__track_" + e;
            },
            buttonEnd: function (e) {
              return "ps__button-end-" + e;
            },
            consuming: "ps__child--consume",
          },
          c = {
            focus: "ps--focus",
            clicking: "ps--clicking",
            active: function (e) {
              return "ps--active-" + e;
            },
            scrolling: function (e) {
              return "ps--scrolling-" + e;
            },
          },
          d = { x: null, y: null },
          m = { immediately: !1 };
        function E(e, t, u) {
          void 0 === u && (u = {});
          var n = e.element.classList,
            r = c.scrolling(t);
          n.contains(r) ? clearTimeout(d[t]) : n.add(r);
        }
        function _(e, t, u) {
          void 0 === u && (u = {});
          Object.assign(m, u).immediately
            ? e.isAlive && e.element.classList.remove(c.scrolling(t))
            : (d[t] = setTimeout(function () {
                return e.isAlive && e.element.classList.remove(c.scrolling(t));
              }, e.settings.scrollingThreshold));
        }
        var h = function (e) {
            ((this.element = e), (this.handlers = {}));
          },
          A = { isEmpty: { configurable: !0 } };
        ((h.prototype.bind = function (e, t) {
          (void 0 === this.handlers[e] && (this.handlers[e] = []),
            this.handlers[e].push(t),
            this.element.addEventListener(e, t, !1));
        }),
          (h.prototype.unbind = function (e, t) {
            var u = this;
            this.handlers[e] = this.handlers[e].filter(function (n) {
              return !(!t || n === t) || (u.element.removeEventListener(e, n, !1), !1);
            });
          }),
          (h.prototype.unbindAll = function () {
            for (var e in this.handlers) this.unbind(e);
          }),
          (A.isEmpty.get = function () {
            var e = this;
            return Object.keys(this.handlers).every(function (t) {
              return 0 === e.handlers[t].length;
            });
          }),
          Object.defineProperties(h.prototype, A));
        var p = function () {
          this.eventElements = [];
        };
        function g(e) {
          return parseInt(e, 10) || 0;
        }
        ((p.prototype.eventElement = function (e) {
          var t = this.eventElements.filter(function (t) {
            return t.element === e;
          })[0];
          return (t || ((t = new h(e)), this.eventElements.push(t)), t);
        }),
          (p.prototype.bind = function (e, t, u) {
            this.eventElement(e).bind(t, u);
          }),
          (p.prototype.unbind = function (e, t, u) {
            var n = this.eventElement(e);
            (n.unbind(t, u),
              n.isEmpty && this.eventElements.splice(this.eventElements.indexOf(n), 1));
          }),
          (p.prototype.unbindAll = function () {
            (this.eventElements.forEach(function (e) {
              return e.unbindAll();
            }),
              (this.eventElements = []));
          }),
          (p.prototype.once = function (e, t, u) {
            var n = this.eventElement(e);
            n.bind(t, function e(r) {
              (n.unbind(t, e), u(r));
            });
          }));
        var b = {
          isWebKit:
            "undefined" != typeof document && "WebkitAppearance" in document.documentElement.style,
          supportsTouch:
            "undefined" != typeof window &&
            ("ontouchstart" in window ||
              (window.DocumentTouch && document instanceof window.DocumentTouch)),
          supportsIePointer: "undefined" != typeof navigator && navigator.msMaxTouchPoints,
          isChrome:
            "undefined" != typeof navigator && /Chrome/i.test(navigator && navigator.userAgent),
        };
        function C() {
          return new Promise(function (e) {
            requestAnimationFrame(function () {
              requestAnimationFrame(function () {
                e();
              });
            });
          });
        }
        function F(e) {
          if ("function" == typeof window.CustomEvent) return new CustomEvent(e);
          var t = document.createEvent("CustomEvent");
          return (t.initCustomEvent(e, !1, !1, void 0), t);
        }
        var f = function (e, t, u, n, r, o) {
          var a;
          if (
            (void 0 === n && (n = !0),
            void 0 === r && (r = !1),
            void 0 === o && (o = !1),
            "top" === t)
          )
            a = ["contentHeight", "containerHeight", "scrollTop", "y", "up", "down"];
          else {
            if ("left" !== t) throw new Error("A proper axis should be provided");
            a = ["contentWidth", "containerWidth", "scrollLeft", "x", "left", "right"];
          }
          !(function (e, t, u, n, r, o) {
            var a = u[0],
              i = u[1],
              l = u[2],
              s = u[3],
              c = u[4],
              d = u[5];
            void 0 === n && (n = !0);
            void 0 === r && (r = !1);
            void 0 === o && (o = !1);
            var m = e.element;
            if (!e.reach) return;
            ((e.reach[s] = null), m[l] < 1 && (e.reach[s] = "start"));
            m[l] > e[a] - e[i] - 1 && (e.reach[s] = "end");
            t &&
              !r &&
              (m.dispatchEvent(F("ps-scroll-" + s)),
              t < 0
                ? m.dispatchEvent(F("ps-scroll-" + c))
                : t > 0 && m.dispatchEvent(F("ps-scroll-" + d)),
              n &&
                (function (e, t) {
                  (E(e, t), _(e, t));
                })(e, s));
            e.reach[s] && (t || o) && m.dispatchEvent(F("ps-" + s + "-reach-" + e.reach[s]));
          })(e, u, a, n, r, o);
        };
        var D = function (e, t, n, r) {
          (void 0 === t && (t = !1), void 0 === n && (n = 0), void 0 === r && (r = !1));
          var o = e.element;
          if (o) {
            if (
              ((e.containerWidth = Math.round(o.getBoundingClientRect().width)),
              (e.containerHeight = Math.round(o.getBoundingClientRect().height)),
              (e.contentWidth = Math.round(o.scrollWidth) - 2 * n),
              (e.contentHeight = Math.round(o.scrollHeight)),
              !r)
            ) {
              e.contentWidth = Math.round(o.scrollWidth) - 2 * n;
              var l = e.contentWidth - e.containerWidth + n;
              o.scrollLeft < n ? (o.scrollLeft = n) : o.scrollLeft > l && (o.scrollLeft = l);
            }
            var d = Math.floor(o.scrollTop),
              m = Math.floor(o.scrollLeft) - n,
              E = parseFloat(getComputedStyle(document.documentElement).fontSize);
            (o.contains(e.scrollbarXRail) ||
              (i(o, s.rail("x")).forEach(function (e) {
                return a(e);
              }),
              o.appendChild(e.scrollbarXRail)),
              o.contains(e.scrollbarYRail) ||
                (i(o, s.rail("y")).forEach(function (e) {
                  return a(e);
                }),
                o.appendChild(e.scrollbarYRail)),
              !e.settings.suppressScrollX &&
              e.containerWidth + e.settings.scrollXMarginOffset < e.contentWidth
                ? ((e.scrollbarXActive = !0),
                  (e.railXWidth = e.containerWidth - e.railXMarginWidth * E - 15 * E),
                  (e.railXRatio = e.containerWidth / e.railXWidth),
                  (e.scrollbarXWidth = v(e, g((e.railXWidth * e.containerWidth) / e.contentWidth))),
                  (e.scrollbarXLeft = g(
                    ((e.negativeScrollAdjustment + m) * (e.railXWidth - e.scrollbarXWidth)) /
                      (e.contentWidth - e.containerWidth),
                  )),
                  e.scrollbarXLeft < 0 && (e.scrollbarXLeft = 0))
                : (e.scrollbarXActive = !1),
              !e.settings.suppressScrollY &&
              e.containerHeight + e.settings.scrollYMarginOffset < e.contentHeight
                ? ((e.scrollbarYActive = !0),
                  (e.railYHeight = e.containerHeight - e.railYMarginHeight * E - 15 * E),
                  (e.railYRatio = e.containerHeight / e.railYHeight),
                  (e.scrollbarYHeight = v(
                    e,
                    g((e.railYHeight * e.containerHeight) / e.contentHeight),
                  )),
                  (e.scrollbarYTop = g(
                    (d * (e.railYHeight - e.scrollbarYHeight)) /
                      (e.contentHeight - e.containerHeight),
                  )))
                : (e.scrollbarYActive = !1),
              e.scrollbarXLeft >= e.railXWidth - e.scrollbarXWidth &&
                (e.scrollbarXLeft = e.railXWidth - e.scrollbarXWidth),
              e.scrollbarYTop >= e.railYHeight - e.scrollbarYHeight &&
                (e.scrollbarYTop = e.railYHeight - e.scrollbarYHeight),
              (function (e, t, n) {
                var r = { width: t.railXWidth },
                  o = Math.floor(e.scrollTop);
                t.isRtl
                  ? (r.left =
                      t.negativeScrollAdjustment + e.scrollLeft + t.containerWidth - t.contentWidth)
                  : (r.left = e.scrollLeft);
                t.isScrollbarXUsingBottom
                  ? (r.bottom = t.scrollbarXBottom - o)
                  : (r.top = t.scrollbarXTop + o);
                u(t.scrollbarXRail, r);
                var a = { top: o, height: t.railYHeight };
                t.isScrollbarYUsingRight
                  ? t.isRtl
                    ? (a.right =
                        t.contentWidth -
                        (t.negativeScrollAdjustment + e.scrollLeft) -
                        t.scrollbarYRight -
                        t.scrollbarYOuterWidth)
                    : (a.right = t.scrollbarYRight - e.scrollLeft)
                  : t.isRtl
                    ? (a.left =
                        t.negativeScrollAdjustment +
                        e.scrollLeft +
                        2 * t.containerWidth -
                        t.contentWidth -
                        t.scrollbarYLeft -
                        t.scrollbarYOuterWidth)
                    : (a.left = t.scrollbarYLeft + e.scrollLeft);
                (u(t.scrollbarYRail, a),
                  u(t.scrollbarX, {
                    left: t.scrollbarXLeft,
                    width: t.scrollbarXWidth - t.railBorderXWidth * n,
                  }),
                  u(t.scrollbarY, {
                    top: t.scrollbarYTop,
                    height: t.scrollbarYHeight - t.railBorderYWidth * n,
                  }));
              })(o, e, E),
              e.scrollbarXButtonStart.classList.toggle("disabled", m < 1),
              e.scrollbarXButtonEnd.classList.toggle(
                "disabled",
                m + e.containerWidth >= e.contentWidth,
              ),
              e.scrollbarYButtonStart.classList.toggle("disabled", o.scrollTop < 1),
              e.scrollbarYButtonEnd.classList.toggle(
                "disabled",
                o.scrollTop + e.containerHeight >= e.contentHeight,
              ),
              e.scrollbarXActive
                ? (o.classList.add(c.active("x")), f(e, "left", m - e.lastScrollLeft, !0, t))
                : (o.classList.remove(c.active("x")),
                  (e.scrollbarXWidth = 0),
                  (e.scrollbarXLeft = 0),
                  (o.scrollLeft = 0)),
              e.scrollbarYActive
                ? (o.classList.add(c.active("y")),
                  f(e, "top", o.scrollTop - e.lastScrollTop, !0, t))
                : (o.classList.remove(c.active("y")),
                  (e.scrollbarYHeight = 0),
                  (e.scrollbarYTop = 0),
                  (o.scrollTop = 0)),
              (e.lastScrollTop = d),
              (e.lastScrollLeft = m),
              (e.scrollTopPercent = o.scrollTop / o.scrollHeight),
              (e.scrollLeftPercent = o.scrollLeft / o.scrollWidth));
          }
        };
        function v(e, t) {
          return (
            e.settings.minScrollbarLength && (t = Math.max(t, e.settings.minScrollbarLength)),
            e.settings.maxScrollbarLength && (t = Math.min(t, e.settings.maxScrollbarLength)),
            t
          );
        }
        var B = {
            linear: function (e) {
              return e;
            },
            easeInQuad: function (e) {
              return e * e;
            },
            easeOutQuad: function (e) {
              return e * (2 - e);
            },
            easeInOutQuad: function (e) {
              return e < 0.5 ? 2 * e * e : (4 - 2 * e) * e - 1;
            },
            easeInCubic: function (e) {
              return e * e * e;
            },
            easeOutCubic: function (e) {
              return --e * e * e + 1;
            },
            easeInOutCubic: function (e) {
              return e < 0.5 ? 4 * e * e * e : (e - 1) * (2 * e - 2) * (2 * e - 2) + 1;
            },
            easeInQuart: function (e) {
              return e * e * e * e;
            },
            easeOutQuart: function (e) {
              return 1 - --e * e * e * e;
            },
            easeInOutQuart: function (e) {
              return e < 0.5 ? 8 * e * e * e * e : 1 - 8 * --e * e * e * e;
            },
            easeInQuint: function (e) {
              return e * e * e * e * e;
            },
            easeOutQuint: function (e) {
              return 1 + --e * e * e * e * e;
            },
            easeInOutQuint: function (e) {
              return e < 0.5 ? 16 * e * e * e * e * e : 1 + 16 * --e * e * e * e * e;
            },
          },
          w = function (e) {
            var t,
              u = e.percentTimeElapsed,
              n = e.x1,
              r = e.y1,
              o = e.x2,
              a = e.y2;
            return (
              1 -
              (n * ((t = u), Math.pow(t, 3)) +
                r *
                  (function (e) {
                    return 3 * e * e * (1 - e);
                  })(u) +
                o *
                  (function (e) {
                    return 3 * e * Math.pow(1 - e, 2);
                  })(u) +
                a *
                  (function (e) {
                    return Math.pow(1 - e, 3);
                  })(u))
            );
          },
          S = { breakBounds: !1, startBound: 0, endBound: 0 },
          y = function (e) {
            var t = e.scrollableDomEle,
              u = e.onAnimationCompleteCallback,
              n = e.direction,
              r = e.onRefUpdateCallback,
              o = e.duration,
              a = e.cubicBezierPoints,
              i = e.easingPreset,
              l = e.scrollAmount,
              s = e.onCheckForBreakCallback,
              c = e.boundsInfo;
            void 0 === c && (c = S);
            var d = null,
              m = null,
              E = null,
              _ = null,
              h = t === window,
              A = ["left", "right"].indexOf(n) > -1,
              p = ["right", "bottom"].indexOf(n) > -1;
            A
              ? ((m = h ? "scrollX" : "scrollLeft"),
                (_ = h ? "innerWidth" : "width"),
                (E = "scrollWidth"))
              : ((m = h ? "scrollY" : "scrollTop"),
                (_ = h ? "innerHeight" : "height"),
                (E = "scrollHeight"));
            var g = t[m],
              b = (function (e) {
                var t,
                  u = e.isWindow,
                  n = e.scrollableDomEle,
                  r = e.elementLengthProp,
                  o = e.initialScrollPosition,
                  a = e.isHorizontalDirection,
                  i = e.scrollLengthProp,
                  l = e.direction;
                if (u) {
                  var s = document.documentElement;
                  t = a ? s.offsetWidth : s.offsetHeight;
                } else t = (n[i] - n.getBoundingClientRect()[r]) | 0;
                return ["left", "top"].includes(l) ? o : t - o;
              })({
                isWindow: h,
                scrollableDomEle: t,
                elementLengthProp: _,
                initialScrollPosition: g,
                isHorizontalDirection: A,
                scrollLengthProp: E,
                direction: n,
              });
            !isNaN(l) && l < b && (b = l);
            var C = function e(n) {
              if (!s || !s()) {
                var l = n - d,
                  E = (function (e) {
                    var t = e.easingPreset,
                      u = e.cubicBezierPoints,
                      n = e.duration,
                      r = e.runTime / n;
                    if (B.hasOwnProperty(t)) return B[t](r);
                    if (
                      u &&
                      !isNaN(u.x1) &&
                      !isNaN(u.y1) &&
                      !isNaN(u.x2) &&
                      !isNaN(u.y2) &&
                      u.x1 >= 0 &&
                      u.x2 >= 0
                    )
                      return w({ percentTimeElapsed: r, x1: u.x1, x2: u.x2, y1: u.y1, y2: u.y2 });
                    throw new Error("Please enter a valid easing value");
                  })({ easingPreset: i, cubicBezierPoints: a, runTime: l, duration: o });
                if (!isNaN(E)) {
                  var _ = Math.round(E * b),
                    C = p ? _ + g : b - _;
                  if (
                    (c.breakBounds &&
                      (C < c.startBound ? (C = c.startBound) : C > c.endBound && (C = c.endBound)),
                    l < o)
                  ) {
                    if (h) {
                      var F = A ? C : 0,
                        f = A ? 0 : C;
                      window.scrollTo(F, f);
                    } else t[m] = C;
                    (r && r(C), requestAnimationFrame(e));
                  } else u && u();
                }
              }
            };
            requestAnimationFrame(function (e) {
              ((d = e), C(e));
            });
          },
          x = function (e) {
            var t = e.axis,
              u = e.cursorPositionOnRail,
              n = e.direction,
              r = e.i,
              o = (function (e) {
                var t = e.axis,
                  u = e.i,
                  n = e.cursorPositionOnRail;
                if ("y" === t) {
                  var r = u.scrollbarY.offsetTop,
                    o = r + u.scrollbarYHeight;
                  return n >= r && n <= o;
                }
                var a = u.scrollbarX.offsetLeft,
                  i = a + u.scrollbarXWidth;
                return n >= a && n <= i;
              })({ axis: t, i: r, cursorPositionOnRail: u });
            return o
              ? ((function (e) {
                  var t = e.axis,
                    u = e.i,
                    n = e.cursorPositionOnRail,
                    r = (function (e, t) {
                      if ("y" === e) {
                        var u = t.contentHeight - t.containerHeight;
                        return {
                          rail: t.railYHeight,
                          content: t.contentHeight,
                          scrollbar: t.scrollbarYHeight,
                          maxScroll: u,
                        };
                      }
                      var n = t.contentWidth - t.containerWidth;
                      return {
                        rail: t.railXWidth,
                        content: t.contentWidth,
                        scrollbar: t.scrollbarXWidth,
                        maxScroll: n,
                      };
                    })(t, u),
                    o = (n - r.scrollbar / 2) / r.rail,
                    a = Math.round(Math.min(r.maxScroll, Math.max(0, r.content * o)));
                  "y" === t ? (u.element.scrollTop = a) : (u.element.scrollLeft = a);
                })({ axis: t, i: r, cursorPositionOnRail: u }),
                !0)
              : ("y" === t
                  ? (r.element.scrollTop += n * r.containerHeight)
                  : (r.element.scrollLeft += n * r.containerWidth),
                !1);
          },
          T = function (e, t, u) {
            return function (n) {
              t = t.toLowerCase();
              var r = null,
                o = function () {
                  if (1 === n.buttons) {
                    if (
                      !n.target.closest(".ps__rail-" + t) ||
                      !n.target.closest(".ps__track_" + t)
                    ) {
                      var o = (function (e) {
                          var t = e.axis,
                            u = e.e,
                            n = e.i;
                          return "y" === t
                            ? {
                                cursorPosition: u.screenY,
                                windowScrolled: window.pageYOffset,
                                elementPosition: n.scrollbarYRail.getBoundingClientRect().top,
                              }
                            : {
                                cursorPosition: u.screenX,
                                windowScrolled: window.pageXOffset,
                                elementPosition: n.scrollbarXRail.getBoundingClientRect().left,
                              };
                        })({ axis: t, e: n, i: e }),
                        a = o.cursorPosition - o.windowScrolled - o.elementPosition,
                        i = (function (e) {
                          var t = e.axis,
                            u = e.cursorPositionOnRail,
                            n = e.i;
                          return u > ("y" === t ? n.scrollbarYTop : n.scrollbarXLeft) ? 1 : -1;
                        })({ axis: t, cursorPositionOnRail: a, i: e });
                      (x({ axis: t, cursorPositionOnRail: a, direction: i, i: e }) &&
                        clearTimeout(r),
                        D(e, !1, u));
                    }
                    n.stopPropagation();
                  }
                };
              (o(),
                (r = setInterval(o, 100)),
                e.event.once(e.ownerDocument, "mouseup", function () {
                  clearTimeout(r);
                }));
            };
          };
        function L(e, t, u) {
          var n = u[0],
            r = u[1],
            o = u[2],
            a = u[3],
            i = u[4],
            l = u[5],
            s = u[6],
            d = u[7],
            m = u[8],
            h = e.element,
            A = null,
            p = null,
            b = null;
          function C(u) {
            ((h[s] = g(A + b * (u[o] - p))),
              E(e, d),
              D(e, !1, t),
              u.stopPropagation(),
              u.preventDefault());
          }
          function F() {
            (_(e, d),
              e[m].classList.remove(c.clicking),
              e.event.unbind(e.ownerDocument, "mousemove", C));
          }
          e.event.bind(e[i], "mousedown", function (t) {
            1 === t.buttons &&
              ((A = h[s]),
              (p = t[o]),
              (b = (e[r] - e[n]) / (e[a] - e[l])),
              e.event.bind(e.ownerDocument, "mousemove", C),
              e.event.once(e.ownerDocument, "mouseup", F),
              e[m].classList.add(c.clicking),
              t.stopPropagation(),
              t.preventDefault());
          });
        }
        var M = 1e3,
          R = {
            "click-rail": function (e, t) {
              (e.event.bind(e.scrollbarY, "mousedown", function (e) {
                return e.stopPropagation();
              }),
                e.event.bind(e.scrollbarYRail, "mousedown", T(e, "y", 0)),
                e.event.bind(e.scrollbarX, "mousedown", function (e) {
                  return e.stopPropagation();
                }),
                e.event.bind(e.scrollbarXRail, "mousedown", T(e, "x", t)));
            },
            "drag-thumb": function (e, t) {
              (L(e, t, [
                "containerWidth",
                "contentWidth",
                "screenX",
                "railXWidth",
                "scrollbarX",
                "scrollbarXWidth",
                "scrollLeft",
                "x",
                "scrollbarXRail",
              ]),
                L(e, t, [
                  "containerHeight",
                  "contentHeight",
                  "screenY",
                  "railYHeight",
                  "scrollbarY",
                  "scrollbarYHeight",
                  "scrollTop",
                  "y",
                  "scrollbarYRail",
                ]));
            },
            keyboard: function (e, t) {
              var u = e.element;
              e.event.bind(e.ownerDocument, "keydown", function (n) {
                if (
                  !((n.isDefaultPrevented && n.isDefaultPrevented()) || n.defaultPrevented) &&
                  o(u, ":hover")
                ) {
                  var r,
                    a = document.activeElement
                      ? document.activeElement
                      : e.ownerDocument.activeElement;
                  if (a) {
                    if ("IFRAME" === a.tagName) a = a.contentDocument.activeElement;
                    else for (; a.shadowRoot;) a = a.shadowRoot.activeElement;
                    if (
                      o((r = a), "input,[contenteditable]") ||
                      o(r, "select,[contenteditable]") ||
                      o(r, "textarea,[contenteditable]") ||
                      o(r, "button,[contenteditable]")
                    )
                      return;
                  }
                  var i = 0,
                    l = 0;
                  switch (n.which) {
                    case 37:
                      i = n.metaKey ? -e.contentWidth : n.altKey ? -e.containerWidth : -30;
                      break;
                    case 38:
                      l = n.metaKey ? e.contentHeight : n.altKey ? e.containerHeight : 30;
                      break;
                    case 39:
                      i = n.metaKey ? e.contentWidth : n.altKey ? e.containerWidth : 30;
                      break;
                    case 40:
                      l = n.metaKey ? -e.contentHeight : n.altKey ? -e.containerHeight : -30;
                      break;
                    case 32:
                      l = n.shiftKey ? e.containerHeight : -e.containerHeight;
                      break;
                    case 33:
                      l = e.containerHeight;
                      break;
                    case 34:
                      l = -e.containerHeight;
                      break;
                    case 36:
                      l = e.contentHeight;
                      break;
                    case 35:
                      l = -e.contentHeight;
                      break;
                    default:
                      return;
                  }
                  (e.settings.suppressScrollX && 0 !== i) ||
                    (e.settings.suppressScrollY && 0 !== l) ||
                    ((u.scrollTop -= l),
                    (u.scrollLeft += i),
                    D(e, !1, t),
                    (function (t, n) {
                      var r = Math.floor(u.scrollTop);
                      if (0 === t) {
                        if (!e.scrollbarYActive) return !1;
                        if (
                          (0 === r && n > 0) ||
                          (r >= e.contentHeight - e.containerHeight && n < 0)
                        )
                          return !e.settings.wheelPropagation;
                      }
                      var o = u.scrollLeft;
                      if (0 === n) {
                        if (!e.scrollbarXActive) return !1;
                        if ((0 === o && t < 0) || (o >= e.contentWidth - e.containerWidth && t > 0))
                          return !e.settings.wheelPropagation;
                      }
                      return !0;
                    })(i, l) && n.preventDefault());
                }
              });
            },
            wheel: function (e, u) {
              var n = e.element;
              function r(r) {
                var o = (function (e) {
                    var t = -1 * e.deltaX,
                      u = e.deltaY;
                    return (
                      (void 0 !== t && void 0 !== u) ||
                        ((t = (-1 * e.wheelDeltaX) / 6), (u = e.wheelDeltaY / 6)),
                      e.deltaMode && 1 === e.deltaMode && ((t *= 10), (u *= 10)),
                      t != t && u != u && ((t = 0), (u = e.wheelDelta)),
                      e.shiftKey ? [-u, -t] : [t, u]
                    );
                  })(r),
                  a = o[0],
                  i = o[1];
                if (
                  !(function (e, u, r) {
                    if (!b.isWebKit && n.querySelector("select")) return !0;
                    if (!n.contains(e)) return !1;
                    for (var o = e; o && o !== n;) {
                      if (o.classList.contains(s.consuming)) return !0;
                      var a = t(o);
                      if ([a.overflow, a.overflowX, a.overflowY].join("").match(/(scroll|auto)/)) {
                        var i = o.scrollHeight - o.clientHeight;
                        if (
                          i > 0 &&
                          !((0 === o.scrollTop && r > 0) || (o.scrollTop === i && r < 0))
                        )
                          return !0;
                        var l = o.scrollWidth - o.clientWidth;
                        if (
                          l > 0 &&
                          !((0 === o.scrollLeft && u < 0) || (o.scrollLeft === l && u > 0))
                        )
                          return !0;
                      }
                      o = o.parentNode;
                    }
                    return !1;
                  })(r.target, a, i)
                ) {
                  var l = !1,
                    c = (a * e.settings.wheelSpeed) | 0,
                    d = (i * e.settings.wheelSpeed) | 0;
                  (e.settings.useBothWheelAxes
                    ? e.scrollbarYActive && !e.scrollbarXActive
                      ? (i ? (n.scrollTop -= d) : (n.scrollTop += c), (l = !0))
                      : e.scrollbarXActive &&
                        !e.scrollbarYActive &&
                        (a ? (n.scrollLeft += c) : (n.scrollLeft -= d), (l = !0))
                    : ((n.scrollTop -= d), (n.scrollLeft += c)),
                    D(e, !1, u),
                    (l =
                      l ||
                      (function (t, u) {
                        var r = Math.floor(n.scrollTop),
                          o = 0 === n.scrollTop,
                          a = r + n.offsetHeight === n.scrollHeight,
                          i = 0 === n.scrollLeft,
                          l = n.scrollLeft + n.offsetWidth === n.scrollWidth;
                        return (
                          !(Math.abs(u) > Math.abs(t) ? o || a : i || l) ||
                          !e.settings.wheelPropagation
                        );
                      })(a, i)),
                    l && !r.ctrlKey && (r.stopPropagation(), r.preventDefault()));
                }
              }
              (e.event.bind(n, "wheel", r),
                void 0 !== window.onmousewheel && e.event.bind(n, "mousewheel", r));
            },
            touch: function (e, u) {
              if (b.supportsTouch || b.supportsIePointer) {
                var n = e.element,
                  r = {},
                  o = 0,
                  a = {},
                  i = null;
                b.supportsTouch
                  ? (e.event.bind(n, "touchstart", m),
                    e.event.bind(n, "touchmove", E),
                    e.event.bind(n, "touchend", _))
                  : b.supportsIePointer &&
                    (window.PointerEvent
                      ? (e.event.bind(n, "pointerdown", m),
                        e.event.bind(n, "pointermove", E),
                        e.event.bind(n, "pointerup", _))
                      : window.MSPointerEvent &&
                        (e.event.bind(n, "MSPointerDown", m),
                        e.event.bind(n, "MSPointerMove", E),
                        e.event.bind(n, "MSPointerUp", _)));
              }
              function l(t, r) {
                ((n.scrollTop -= r), (n.scrollLeft -= t), D(e, !1, u));
              }
              function c(e) {
                return e.targetTouches ? e.targetTouches[0] : e;
              }
              function d(e) {
                return (
                  (!e.pointerType || "pen" !== e.pointerType || 0 !== e.buttons) &&
                  (!(!e.targetTouches || 1 !== e.targetTouches.length) ||
                    !(
                      !e.pointerType ||
                      "mouse" === e.pointerType ||
                      e.pointerType === e.MSPOINTER_TYPE_MOUSE
                    ))
                );
              }
              function m(e) {
                if (d(e)) {
                  var t = c(e);
                  ((r.pageX = t.pageX),
                    (r.pageY = t.pageY),
                    (o = new Date().getTime()),
                    null !== i && clearInterval(i));
                }
              }
              function E(u) {
                if (d(u)) {
                  var i = c(u),
                    m = { pageX: i.pageX, pageY: i.pageY },
                    E = m.pageX - r.pageX,
                    _ = m.pageY - r.pageY;
                  if (
                    (function (e, u, r) {
                      if (!n.contains(e)) return !1;
                      for (var o = e; o && o !== n;) {
                        if (o.classList.contains(s.consuming)) return !0;
                        var a = t(o);
                        if (
                          [a.overflow, a.overflowX, a.overflowY].join("").match(/(scroll|auto)/)
                        ) {
                          var i = o.scrollHeight - o.clientHeight;
                          if (
                            i > 0 &&
                            !((0 === o.scrollTop && r > 0) || (o.scrollTop === i && r < 0))
                          )
                            return !0;
                          var l = o.scrollLeft - o.clientWidth;
                          if (
                            l > 0 &&
                            !((0 === o.scrollLeft && u < 0) || (o.scrollLeft === l && u > 0))
                          )
                            return !0;
                        }
                        o = o.parentNode;
                      }
                      return !1;
                    })(u.target, E, _)
                  )
                    return;
                  (l(E, _), (r = m));
                  var h = new Date().getTime(),
                    A = h - o;
                  (A > 0 && ((a.x = E / A), (a.y = _ / A), (o = h)),
                    (function (t, u) {
                      var r = Math.floor(n.scrollTop),
                        o = n.scrollLeft,
                        a = Math.abs(t),
                        i = Math.abs(u);
                      if (i > a) {
                        if (
                          (u < 0 && r === e.contentHeight - e.containerHeight) ||
                          (u > 0 && 0 === r)
                        )
                          return 0 === window.scrollY && u > 0 && b.isChrome;
                      } else if (
                        a > i &&
                        ((t < 0 && o === e.contentWidth - e.containerWidth) || (t > 0 && 0 === o))
                      )
                        return !0;
                      return !0;
                    })(E, _) && u.preventDefault());
                }
              }
              function _() {
                e.settings.swipeEasing &&
                  (clearInterval(i),
                  (i = setInterval(function () {
                    e.isInitialized
                      ? clearInterval(i)
                      : a.x || a.y
                        ? Math.abs(a.x) < 0.01 && Math.abs(a.y) < 0.01
                          ? clearInterval(i)
                          : (l(30 * a.x, 30 * a.y), (a.x *= 0.8), (a.y *= 0.8))
                        : clearInterval(i);
                  }, 10)));
              }
            },
            "drag-move": function (e, t) {
              void 0 === t && (t = 0);
              var u = e.element,
                n = null,
                r = !1,
                o = 0,
                a = 0,
                i = 0;
              function l() {
                e.onScroll();
              }
              function s(n, r, o, a) {
                (void 0 === o && (o = null),
                  void 0 === a && (a = !1),
                  y({
                    scrollableDomEle: u,
                    direction: "right",
                    onRefUpdateCallback: l,
                    duration: r,
                    easingPreset: "easeOutCubic",
                    scrollAmount: n,
                    onCheckForBreakCallback: o,
                    boundsInfo: {
                      breakBounds: a,
                      startBound: t,
                      endBound: e.contentWidth - e.containerWidth + t,
                    },
                  }));
              }
              function d() {
                if (r) return r;
              }
              function m() {
                i = 0;
              }
              function h(r) {
                if (e.scrollbarXActive) {
                  var l = n - r.screenX;
                  ((u.scrollLeft += l), (n = r.screenX));
                  var s = new Date().getTime();
                  if (((o = (l / (s - a)) * 1e3), (a = s), e.onScroll(), t > 0)) {
                    var c = e.contentWidth - e.containerWidth + 2 * t;
                    0 === u.scrollLeft || u.scrollLeft === c
                      ? 0 === i && (i = window.setTimeout(m, 250))
                      : 0 !== i && (window.clearTimeout(i), (i = 0));
                  }
                  (E(e, "x"),
                    E(e, "dragging", { immediately: !0 }),
                    r.stopPropagation(),
                    r.preventDefault());
                }
              }
              function A(e) {
                ((n = e.screenX),
                  (r = !0),
                  requestAnimationFrame(function () {
                    r = !1;
                  }),
                  (a = new Date().getTime()));
              }
              function p(n) {
                var r = e.contentWidth - e.containerWidth + t;
                if (u.scrollLeft < t) s(t - u.scrollLeft, M, d);
                else if (u.scrollLeft > r) s(r - u.scrollLeft, M, d);
                else {
                  new Date().getTime() - a < 100 && s(o / 4, M, d, !0);
                }
                (_(e, "x"),
                  _(e, "dragging", { immediately: !0 }),
                  e.scrollbarXRail.classList.remove(c.clicking),
                  e.event.unbind(e.ownerDocument, "mousemove", h));
              }
              function g() {
                r = !0;
              }
              u.addEventListener(
                "mousedown",
                function (t) {
                  1 === t.buttons &&
                    ((n = t.screenX),
                    e.event.bind(e.ownerDocument, "mousemove", h),
                    e.event.once(e.ownerDocument, "mouseup", p),
                    e.event.once(e.ownerDocument, "mousedown", A),
                    e.event.once(u, "wheel", g),
                    e.scrollbarXRail.classList.add(c.clicking),
                    t.preventDefault());
                },
                !1,
              );
            },
          },
          k = function (e, r) {
            var o = this;
            if (
              (void 0 === r && (r = {}),
              "string" == typeof e && (e = document.querySelector(e)),
              !e || !e.nodeName)
            )
              throw new Error("no element is specified to initialize PerfectScrollbar");
            for (var a in ((this.element = e),
            e.classList.add(l),
            (this.settings = {
              handlers: ["click-rail", "drag-thumb", "keyboard", "wheel", "touch", "drag-move"],
              maxScrollbarLength: null,
              minScrollbarLength: null,
              scrollingThreshold: 1e3,
              scrollXMarginOffset: 0,
              scrollYMarginOffset: 0,
              suppressScrollX: !1,
              suppressScrollY: !1,
              swipeEasing: !0,
              useBothWheelAxes: !1,
              wheelPropagation: !0,
              wheelSpeed: 10,
              enableHorizontalScroll: !1,
              animationDuration: 1e3,
              animationEasingPreset: "easeInOutQuint",
              isDisableScrollToLastPositionOnResize: !1,
              overScrollWidth: 0,
            }),
            r))
              o.settings[a] = r[a];
            ((this.containerWidth = null),
              (this.containerHeight = null),
              (this.contentWidth = null),
              (this.contentHeight = null));
            var i,
              d,
              m = function () {
                return e.classList.add(c.focus);
              },
              E = function () {
                return e.classList.remove(c.focus);
              };
            ((this.isRtl = "rtl" === t(e).direction),
              (this.isNegativeScroll =
                ((d = e.scrollLeft),
                (e.scrollLeft = -1),
                (i = e.scrollLeft < 0),
                (e.scrollLeft = d),
                i)),
              (this.negativeScrollAdjustment = this.isNegativeScroll
                ? e.scrollWidth - e.clientWidth
                : 0),
              (this.event = new p()),
              (this.ownerDocument = e.ownerDocument || document),
              (this.scrollbarXRail = n(s.rail("x"))),
              (this.scrollbarXButtonStart = n(s.buttonStart("x"))),
              (this.scrollbarXButtonEnd = n(s.buttonEnd("x"))),
              (this.scrollbarXTrack = n(s.track("x"))),
              e.appendChild(this.scrollbarXRail),
              this.scrollbarXRail.appendChild(this.scrollbarXTrack),
              this.scrollbarXRail.appendChild(this.scrollbarXButtonStart),
              this.scrollbarXRail.appendChild(this.scrollbarXButtonEnd),
              (this.scrollbarX = n(s.thumb("x"))),
              this.scrollbarXRail.appendChild(this.scrollbarX),
              this.scrollbarX.setAttribute("tabindex", 0),
              this.event.bind(this.scrollbarX, "focus", m),
              this.event.bind(this.scrollbarX, "blur", E),
              (this.scrollbarXActive = null),
              (this.scrollbarXWidth = null),
              (this.scrollbarXLeft = null),
              (this.scrollbarYRail = n(s.rail("y"))),
              (this.scrollbarYButtonStart = n(s.buttonStart("y"))),
              (this.scrollbarYButtonEnd = n(s.buttonEnd("y"))),
              (this.scrollbarYTrack = n(s.track("y"))),
              e.appendChild(this.scrollbarYRail),
              this.scrollbarYRail.appendChild(this.scrollbarYTrack),
              this.scrollbarYRail.appendChild(this.scrollbarYButtonStart),
              this.scrollbarYRail.appendChild(this.scrollbarYButtonEnd),
              (this.scrollbarY = n(s.thumb("y"))),
              this.scrollbarYRail.appendChild(this.scrollbarY),
              this.scrollbarY.setAttribute("tabindex", 0),
              this.event.bind(this.scrollbarY, "focus", m),
              this.event.bind(this.scrollbarY, "blur", E),
              (this.scrollbarYActive = null),
              (this.scrollbarYHeight = null),
              (this.scrollbarYTop = null),
              C().then(function () {
                var n = t(o.scrollbarXRail);
                ((o.scrollbarXBottom = parseInt(n.bottom, 10)),
                  isNaN(o.scrollbarXBottom)
                    ? ((o.isScrollbarXUsingBottom = !1), (o.scrollbarXTop = g(n.top)))
                    : (o.isScrollbarXUsingBottom = !0),
                  (o.railBorderXWidth = g(n.borderLeftWidth) + g(n.borderRightWidth)),
                  u(o.scrollbarXRail, { display: "block" }),
                  (o.railXMarginWidth = g(n.marginLeft) + g(n.marginRight)),
                  u(o.scrollbarXRail, { display: "" }),
                  (o.railXWidth = null),
                  (o.railXRatio = null));
                var r = t(o.scrollbarYRail);
                ((o.scrollbarYRight = parseInt(r.right, 10)),
                  isNaN(o.scrollbarYRight)
                    ? ((o.isScrollbarYUsingRight = !1), (o.scrollbarYLeft = g(r.left)))
                    : (o.isScrollbarYUsingRight = !0),
                  (o.scrollbarYOuterWidth = o.isRtl
                    ? (function (e) {
                        var u = t(e);
                        return (
                          g(u.width) +
                          g(u.paddingLeft) +
                          g(u.paddingRight) +
                          g(u.borderLeftWidth) +
                          g(u.borderRightWidth)
                        );
                      })(o.scrollbarY)
                    : null),
                  (o.railBorderYWidth = g(r.borderTopWidth) + g(r.borderBottomWidth)),
                  u(o.scrollbarYRail, { display: "block" }),
                  (o.railYMarginHeight = g(r.marginTop) + g(r.marginBottom)),
                  u(o.scrollbarXRail, { display: "" }),
                  u(o.scrollbarYRail, { display: "" }),
                  (o.railYHeight = null),
                  (o.railYRatio = null),
                  (o.reach = {
                    x:
                      e.scrollLeft <= 0
                        ? "start"
                        : e.scrollLeft >= o.contentWidth - o.containerWidth
                          ? "end"
                          : null,
                    y:
                      e.scrollTop <= 0
                        ? "start"
                        : e.scrollTop >= o.contentHeight - o.containerHeight
                          ? "end"
                          : null,
                  }),
                  (o.isAlive = !0),
                  o.settings.handlers.forEach(function (e) {
                    return R[e](o, o.settings.overScrollWidth);
                  }),
                  (o.boundHandleButtonEnter = o.handleMouseEnter.bind(o)),
                  (o.boundHandleMouseLeave = o.handleMouseLeave.bind(o)),
                  (o.boundHandleMouseEnter = o.handleMouseEnter.bind(o)),
                  (o.boundPlayClickSound = o.playClickSound.bind(o)),
                  o.scrollbarYButtonStart.addEventListener("mousedown", o.boundPlayClickSound),
                  o.scrollbarYButtonEnd.addEventListener("mousedown", o.boundPlayClickSound),
                  o.scrollbarXButtonStart.addEventListener("mousedown", o.boundPlayClickSound),
                  o.scrollbarXButtonEnd.addEventListener("mousedown", o.boundPlayClickSound),
                  o.scrollbarXButtonStart.addEventListener("mouseenter", o.boundHandleMouseEnter),
                  o.scrollbarXButtonEnd.addEventListener("mouseenter", o.boundHandleMouseEnter),
                  o.scrollbarYButtonStart.addEventListener("mouseenter", o.boundHandleButtonEnter),
                  o.scrollbarYButtonEnd.addEventListener("mouseenter", o.boundHandleButtonEnter),
                  o.scrollbarYButtonStart.addEventListener("mouseleave", o.boundHandleMouseLeave),
                  o.scrollbarYButtonEnd.addEventListener("mouseleave", o.boundHandleMouseLeave),
                  o.scrollbarY.addEventListener("mouseenter", o.boundHandleMouseEnter),
                  o.scrollbarX.addEventListener("mouseenter", o.boundHandleMouseEnter),
                  o.scrollbarY.addEventListener("mouseleave", o.boundHandleMouseLeave),
                  o.scrollbarY.addEventListener("mousedown", o.boundPlayClickSound),
                  o.scrollbarX.addEventListener("mousedown", o.boundPlayClickSound),
                  (o.lastScrollTop = Math.floor(e.scrollTop)),
                  (o.lastScrollLeft = e.scrollLeft),
                  (o.scrollTopPercent = e.scrollTop / e.scrollHeight),
                  (o.scrollLeftPercent = e.scrollLeft / e.scrollWidth),
                  o.event.bind(o.element, "scroll", function (e) {
                    return o.onScroll(e);
                  }),
                  o.settings.enableHorizontalScroll &&
                    o.event.bind(o.element, "wheel", function (e) {
                      return o.onWheel(e);
                    }),
                  D(o, !1, o.settings.overScrollWidth, !1));
              }));
          };
        ((k.prototype._getAnimationSettings = function (e, t, u, n) {
          var r = this,
            o = 0;
          return (
            null !== this.element &&
              (o = ["bottom", "top"].includes(t)
                ? this.element.scrollTop
                : this.element.scrollLeft),
            {
              scrollableDomEle: this.element,
              duration: this.settings.animationDuration,
              easingPreset: this.settings.animationEasingPreset,
              scrollAmount: e - o,
              direction: t,
              onRefUpdateCallback: function (e) {
                (D(r, !0, r.settings.overScrollWidth, !1), u && u(e));
              },
              onAnimationCompleteCallback: function () {
                n && n();
              },
            }
          );
        }),
          (k.prototype.playHoverSound = function () {
            window.engine && engine.call("PlaySound", "highlight");
          }),
          (k.prototype.playClickSound = function () {
            window.engine && engine.call("PlaySound", "play");
          }),
          (k.prototype.handleMouseEnter = function () {
            this.playHoverSound();
          }),
          (k.prototype.handleMouseLeave = function () {}),
          (k.prototype.update = function () {
            var e = this;
            this.isAlive &&
              ((this.negativeScrollAdjustment = this.isNegativeScroll
                ? this.element.scrollWidth - this.element.clientWidth
                : 0),
              u(this.scrollbarXRail, { display: "block" }),
              u(this.scrollbarYRail, { display: "block" }),
              (this.railXMarginWidth =
                g(t(this.scrollbarXRail).marginLeft) + g(t(this.scrollbarXRail).marginRight)),
              (this.railYMarginHeight =
                g(t(this.scrollbarYRail).marginTop) + g(t(this.scrollbarYRail).marginBottom)),
              u(this.scrollbarXRail, { display: "none" }),
              u(this.scrollbarYRail, { display: "none" }),
              C().then(function () {
                (e.settings.isDisableScrollToLastPositionOnResize ||
                  ((e.element.scrollTop = e.element.scrollHeight * e.scrollTopPercent),
                  (e.element.scrollLeft = e.element.scrollWidth * e.scrollLeftPercent)),
                  D(e, !1, e.settings.overScrollWidth, !1),
                  f(e, "top", 0, !1, !1, !0),
                  f(e, "left", 0, !1, !1, !0),
                  u(e.scrollbarXRail, { display: "" }),
                  u(e.scrollbarYRail, { display: "" }));
              }));
          }),
          (k.prototype.setScrollLeft = function (e, t, u) {
            y(this._getAnimationSettings(e, "right", t, u));
          }),
          (k.prototype.setScrollLeftImmediately = function (e) {
            ((this.element.scrollLeft = 0 | e), this.update());
          }),
          (k.prototype.setScrollTop = function (e, t, u) {
            y(this._getAnimationSettings(e, "bottom", t, u));
          }),
          (k.prototype.setScrollTopImmediately = function (e) {
            ((this.element.scrollTop = 0 | e), this.update());
          }),
          (k.prototype.onScroll = function (e) {
            this.isAlive && D(this, !1, this.settings.overScrollWidth, !0);
          }),
          (k.prototype.onWheel = function (e) {
            this.isAlive &&
              (D(this, !1, this.settings.overScrollWidth, !1),
              f(this, "left", this.element.scrollLeft - this.lastScrollLeft),
              (this.lastScrollLeft = this.element.scrollLeft));
          }),
          (k.prototype.destroy = function () {
            this.isAlive &&
              (this.scrollbarYButtonStart.removeEventListener(
                "mousedown",
                this.boundPlayClickSound,
              ),
              this.scrollbarYButtonEnd.removeEventListener("mousedown", this.boundPlayClickSound),
              this.scrollbarXButtonStart.removeEventListener("mousedown", this.boundPlayClickSound),
              this.scrollbarXButtonEnd.removeEventListener("mousedown", this.boundPlayClickSound),
              this.scrollbarXButtonStart.removeEventListener(
                "mouseenter",
                this.boundHandleMouseEnter,
              ),
              this.scrollbarXButtonEnd.removeEventListener(
                "mouseenter",
                this.boundHandleMouseEnter,
              ),
              this.scrollbarYButtonStart.removeEventListener(
                "mouseenter",
                this.boundHandleButtonEnter,
              ),
              this.scrollbarYButtonEnd.removeEventListener(
                "mouseenter",
                this.boundHandleButtonEnter,
              ),
              this.scrollbarYButtonStart.removeEventListener(
                "mouseleave",
                this.boundHandleMouseLeave,
              ),
              this.scrollbarYButtonEnd.removeEventListener(
                "mouseleave",
                this.boundHandleMouseLeave,
              ),
              this.scrollbarY.removeEventListener("mouseenter", this.boundHandleMouseEnter),
              this.scrollbarX.removeEventListener("mouseenter", this.boundHandleMouseEnter),
              this.scrollbarY.removeEventListener("mouseleave", this.boundHandleMouseLeave),
              this.scrollbarY.removeEventListener("mousedown", this.boundPlayClickSound),
              this.scrollbarX.removeEventListener("mousedown", this.boundPlayClickSound),
              this.event.unbindAll(),
              a(this.scrollbarX),
              a(this.scrollbarY),
              a(this.scrollbarXRail),
              a(this.scrollbarYRail),
              this.removePsClasses(),
              (this.element = null),
              (this.scrollbarX = null),
              (this.scrollbarY = null),
              (this.scrollbarXRail = null),
              (this.scrollbarYRail = null),
              (this.isAlive = !1));
          }),
          (k.prototype.removePsClasses = function () {
            this.element.className = this.element.className
              .split(" ")
              .filter(function (e) {
                return !e.match(/^ps([-_].+|)$/);
              })
              .join(" ");
          }),
          (e.exports = k));
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
      532: (e) => {
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
      887: (e) => {
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
      527: (e, t, u) => {
        "use strict";
        (u.r(t), u.d(t, { mouse: () => i, onResize: () => o }));
        var n = u(472),
          r = u(176);
        const o = (0, n.E)("clientResized"),
          a = { down: (0, n.E)("mousedown"), up: (0, n.E)("mouseup"), move: (0, n.E)("mousemove") };
        const i = (function () {
          const e = { listeners: 0, enabled: !0, initialized: !1 };
          function t() {
            e.enabled && (0, r.R)(!1);
          }
          function u() {
            e.enabled && (0, r.R)(!0);
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
              : (0, r.R)(!1);
          }
          const o = ["down", "up", "move"].reduce(
            (t, u) => (
              (t[u] = (function (t) {
                return (u) => {
                  e.listeners += 1;
                  let r = !0;
                  const o = `mouse${t}`,
                    i = a[t]((e) => u([e, "outside"]));
                  function l(e) {
                    u([e, "inside"]);
                  }
                  return (
                    window.addEventListener(o, l),
                    n(),
                    () => {
                      r &&
                        (i(), window.removeEventListener(o, l), (e.listeners -= 1), n(), (r = !1));
                    }
                  );
                };
              })(u)),
              t
            ),
            {},
          );
          return Object.assign({}, o, {
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
      959: (e, t, u) => {
        "use strict";
        (u.r(t),
          u.d(t, {
            events: () => n,
            getMouseGlobalPosition: () => o,
            getSize: () => r,
            graphicsQuality: () => a,
          }));
        var n = u(527);
        function r(e = "px") {
          return "rem" === e ? viewEnv.getClientSizeRem() : viewEnv.getClientSizePx();
        }
        function o(e = "px") {
          return "rem" === e
            ? viewEnv.getMouseGlobalPositionRem()
            : viewEnv.getMouseGlobalPositionPx();
        }
        const a = {
          isLow: () => 1 === viewEnv.getGraphicsQuality(),
          isHigh: () => 0 === viewEnv.getGraphicsQuality(),
          get: () => viewEnv.getGraphicsQuality(),
        };
      },
      176: (e, t, u) => {
        "use strict";
        function n(e) {
          viewEnv.setTrackMouseOnStage(e);
        }
        u.d(t, { R: () => n });
      },
      472: (e, t, u) => {
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
      138: (e, t, u) => {
        "use strict";
        u.d(t, { O: () => r });
        var n = u(959);
        const r = { view: u(641), client: n };
      },
      722: (e, t, u) => {
        "use strict";
        function n(e, t, u = 1) {
          return viewEnv.getChildTexturePath(e, t.width, t.height, u);
        }
        function r(e, t, u) {
          return `url(${n(e, t, u)})`;
        }
        (u.r(t), u.d(t, { getBgUrl: () => r, getTextureUrl: () => n }));
      },
      112: (e, t, u) => {
        "use strict";
        u.d(t, { W: () => n });
        const n = { showing: 0, shown: 1, hiding: 2, hidden: 3 };
      },
      538: (e, t, u) => {
        "use strict";
        u.d(t, { U: () => r });
        var n = u(472);
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
      641: (e, t, u) => {
        "use strict";
        (u.r(t),
          u.d(t, {
            addModelObserver: () => c,
            addPreloadTexture: () => i,
            children: () => n,
            displayStatus: () => r.W,
            displayStatusIs: () => w,
            events: () => o.U,
            extraSize: () => S,
            forceTriggerMouseMove: () => v,
            freezeTextureBeforeResize: () => h,
            getBrowserTexturePath: () => s,
            getDisplayStatus: () => B,
            getScale: () => A,
            getSize: () => m,
            getViewGlobalPosition: () => _,
            isClientAccessible: () => F,
            isEventHandled: () => D,
            isFocused: () => C,
            pxToRem: () => p,
            remToPx: () => g,
            resize: () => E,
            sendEvent: () => a.qP,
            setAnimateWindow: () => b,
            setEventHandled: () => f,
            setInputPaddingsRem: () => l,
            setSidePaddingsRem: () => d,
            whenTutorialReady: () => y,
          }));
        var n = u(722),
          r = u(112),
          o = u(538),
          a = u(566);
        function i(e) {
          viewEnv.addPreloadTexture(e);
        }
        function l(e) {
          viewEnv.setHitAreaPaddingsRem(e, e, e, e, 15);
        }
        function s(e, t, u, n = 1) {
          return viewEnv.getWebBrowserTexturePath(e, t, u, n);
        }
        function c(e, t, u) {
          return viewEnv.addDataChangedCallback(e, t, u);
        }
        function d(e) {
          viewEnv.setHitAreaPaddingsRem(e.top, e.right, e.bottom, e.left, 15);
        }
        function m(e = "px") {
          return "rem" === e ? viewEnv.getViewSizeRem() : viewEnv.getViewSizePx();
        }
        function E(e, t, u = "px") {
          return "rem" === u ? viewEnv.resizeViewRem(e, t) : viewEnv.resizeViewPx(e, t);
        }
        function _(e = "rem") {
          const t = viewEnv.getViewGlobalPositionRem();
          return "rem" === e ? t : { x: g(t.x), y: g(t.y) };
        }
        function h() {
          viewEnv.freezeTextureBeforeResize();
        }
        function A() {
          return viewEnv.getScale();
        }
        function p(e) {
          return viewEnv.pxToRem(e);
        }
        function g(e) {
          return viewEnv.remToPx(e);
        }
        function b(e, t) {
          viewEnv.setAnimateWindow(e, t);
        }
        function C() {
          return viewEnv.isFocused();
        }
        function F() {
          return viewEnv.isClientAccessible();
        }
        function f() {
          return viewEnv.setEventHandled();
        }
        function D() {
          return viewEnv.isEventHandled();
        }
        function v() {
          viewEnv.forceTriggerMouseMove();
        }
        function B() {
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
          y = Promise.all([
            new Promise((e) => {
              window.isDomBuilt ? e() : o.U.onDomBuilt(e);
            }),
            engine.whenReady,
          ]);
      },
      566: (e, t, u) => {
        "use strict";
        u.d(t, { qP: () => s });
        const n = ["args"];
        const r = 2,
          o = 16,
          a = 32,
          i = 64,
          l = (e, t) => {
            const u = "GFViewEventProxy";
            if (void 0 !== t) {
              const o = t.args,
                a = (function (e, t) {
                  if (null == e) return {};
                  var u,
                    n,
                    r = {},
                    o = Object.keys(e);
                  for (n = 0; n < o.length; n++) ((u = o[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
                  return r;
                })(t, n);
              return void 0 !== o
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: u, type: e }, a, {
                      arguments:
                        ((r = o),
                        Object.entries(r).map(([e, t]) => {
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
                : viewEnv.handleViewEvent(Object.assign({ __Type: u, type: e }, a));
            }
            return viewEnv.handleViewEvent({ __Type: u, type: e });
            var r;
          },
          s = {
            close(e) {
              l("popover" === e ? r : a);
            },
            minimize() {
              l(i);
            },
            move(e) {
              l(o, { isMouseEvent: !0, on: e });
            },
          };
      },
      521: (e, t, u) => {
        "use strict";
        let n, r;
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
          })(r || (r = {})));
      },
      358: (e, t, u) => {
        "use strict";
        u.d(t, { Z: () => o });
        var n = u(138);
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
          addCallback(e, t, u = 0, r = !0) {
            void 0 === this._updateHandler &&
              (this._updateHandler = engine.on(
                "viewEnv.onDataChanged",
                this._emmitDataChanged,
                this,
              ));
            const o = n.O.view.addModelObserver(e, u, r);
            return (
              o > 0
                ? ((this._callbacks[o] = t),
                  u > 0 && (this._views[u] ? this._views[u].push(o) : (this._views[u] = [o])))
                : console.error("Can't add callback for model:", e),
              o
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
        r.__instance = void 0;
        const o = r;
      },
      572: (__unused_webpack_module, __webpack_exports__, __webpack_require__) => {
        "use strict";
        __webpack_require__.d(__webpack_exports__, { Z: () => __WEBPACK_DEFAULT_EXPORT__ });
        var _DataTracker__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(358),
          _index__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(364);
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
      364: (e, t, u) => {
        "use strict";
        u.d(t, {
          Sw: () => o.Z,
          B3: () => s,
          Z5: () => a,
          B0: () => l,
          wU: () => v,
          ry: () => g,
          Eu: () => b,
          SW: () => f,
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
        const r = n;
        var o = u(358);
        const a = {
            getNumberFormat: (e, t) => systemLocale.getNumberFormat(e, t),
            getRealFormat: (e, t) => systemLocale.getRealFormat(e, t),
            getTimeFormat: (e, t) => systemLocale.getTimeFormat(e, t),
            getDateFormat: (e, t) => systemLocale.getDateFormat(e, t),
            toUpperCase: (e) => systemLocale.toUpperCase(e),
            toLowerCase: (e) => systemLocale.toUpperCase(e),
          },
          i = {
            getNumberFormat: (e) => userLocale.getNumberFormat(e),
            getTimeFormat: (e, t, u) => userLocale.getTimeFormat(e, t, void 0 === u || u),
            getTimeString: (e, t, u) => userLocale.getTimeString(e, t, void 0 === u || u),
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
          c = Object.freeze({ FRACTIONAL: 0, WO_ZERO_DIGITS: 1 }),
          d = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1 }),
          m = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1, YEAR_MONTH: 2 });
        var E = u(521),
          _ = u(138);
        const h = ["args"];
        function A(e, t, u, n, r, o, a) {
          try {
            var i = e[o](a),
              l = i.value;
          } catch (e) {
            return void u(e);
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
          g = (function () {
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
                  return new Promise(function (n, r) {
                    var o = e.apply(t, u);
                    function a(e) {
                      A(o, n, r, a, i, "next", e);
                    }
                    function i(e) {
                      A(o, n, r, a, i, "throw", e);
                    }
                    a(void 0);
                  });
                });
            return function () {
              return t.apply(this, arguments);
            };
          })(),
          b = () =>
            new Promise((e) => {
              requestAnimationFrame(() => {
                requestAnimationFrame(() => {
                  e();
                });
              });
            }),
          C = (e, t) => {
            const u = "GFViewEventProxy";
            if (void 0 !== t) {
              const r = t.args,
                o = (function (e, t) {
                  if (null == e) return {};
                  var u,
                    n,
                    r = {},
                    o = Object.keys(e);
                  for (n = 0; n < o.length; n++) ((u = o[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
                  return r;
                })(t, h);
              void 0 !== r
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: u, type: e }, o, {
                      arguments:
                        ((n = r),
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
                : viewEnv.handleViewEvent(Object.assign({ __Type: u, type: e }, o));
            } else viewEnv.handleViewEvent({ __Type: u, type: e });
            var n;
          },
          F = () => C(l.CLOSE),
          f = () => C(l.POP_OVER, { on: !1 }),
          D = (e, t, u, n, r = R.invalid("resId"), o) => {
            const a = _.O.view.getViewGlobalPosition(),
              i = u.getBoundingClientRect(),
              s = i.x,
              c = i.y,
              d = i.width,
              m = i.height,
              E = {
                x: _.O.view.pxToRem(s) + a.x,
                y: _.O.view.pxToRem(c) + a.y,
                width: _.O.view.pxToRem(d),
                height: _.O.view.pxToRem(m),
              };
            C(l.POP_OVER, {
              isMouseEvent: !0,
              contentID: e,
              decoratorID: n || R.invalid("resId"),
              targetID: r,
              direction: t,
              bbox: p(E),
              on: !0,
              args: o,
            });
          },
          v = () => viewEnv.isWindowShownByViewEvent(l.POP_OVER),
          B = (e, t) => {
            e.keyCode === E.n.ESCAPE && t();
          };
        var w = u(572);
        const S = r.instance,
          y = {
            DataTracker: o.Z,
            ViewModel: w.Z,
            ViewEventType: l,
            NumberFormatType: s,
            RealFormatType: c,
            TimeFormatType: d,
            DateFormatType: m,
            makeGlobalBoundingBox: p,
            sendMoveEvent: (e) => C(l.MOVE, { isMouseEvent: !0, on: e }),
            sendCloseEvent: F,
            sendClosePopOverEvent: f,
            sendShowContextMenuEvent: (e, t, u = 0) => {
              C(l.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: e,
                on: !0,
                decoratorID: u,
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
              B(e, F);
            },
            handleViewEvent: C,
            onBindingsReady: g,
            onLayoutReady: b,
            isTooltipShown: () => viewEnv.isWindowShownByViewEvent(l.TOOLTIP),
            isContextMenuShown: () => viewEnv.isWindowShownByViewEvent(l.CONTEXT_MENU),
            isPopOverShown: v,
            dumpViewModel: function e(t) {
              const u = {};
              if ("object" != typeof t) return t;
              for (const n in t)
                if (Object.prototype.hasOwnProperty.call(t, n)) {
                  const r = Object.prototype.toString.call(t[n]);
                  if (r.startsWith("[object CoherentArrayProxy]")) {
                    const r = t[n];
                    u[n] = [];
                    for (let t = 0; t < r.length; t++) u[n].push({ value: e(r[t].value) });
                  } else
                    r.startsWith("[object class BW::WULF::ViewModel")
                      ? (u[n] = e(t[n]))
                      : (u[n] = t[n]);
                }
              return u;
            },
            ClickOutsideManager: S,
            SystemLocale: a,
            UserLocale: i,
          };
        window.ViewEnvHelper = y;
      },
      409: (e, t, u) => {
        "use strict";
        var n = {};
        (u.r(n),
          u.d(n, {
            Area: () => ve,
            Bar: () => Fe,
            DefaultScroll: () => De,
            Direction: () => oe,
            defaultSettings: () => ae,
            useHorizontalScrollApi: () => le,
          }));
        var r = {};
        (u.r(r),
          u.d(r, {
            Area: () => Ye,
            Bar: () => Ie,
            Default: () => Xe,
            useVerticalScrollApi: () => Be,
          }));
        var o = u(179),
          a = u.n(o);
        const i = (e, t, u) =>
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
        var l = u(138);
        const s = {
          extraLarge: { weight: 4, width: 2560, height: 1440 },
          large: { weight: 3, width: 1920, height: 1080 },
          medium: { weight: 2, width: 1600, height: 900 },
          small: { weight: 1, width: 1366, height: 768 },
          extraSmall: { weight: 0, width: 1024, height: 768 },
        };
        var c;
        function d(e, t, u) {
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
            })(t, u),
            o = Math.min(n, r);
          return {
            extraLarge: o === u.extraLarge.weight,
            large: o === u.large.weight,
            medium: o === u.medium.weight,
            small: o === u.small.weight,
            extraSmall: o === u.extraSmall.weight,
            extraLargeWidth: n === u.extraLarge.weight,
            largeWidth: n === u.large.weight,
            mediumWidth: n === u.medium.weight,
            smallWidth: n === u.small.weight,
            extraSmallWidth: n === u.extraSmall.weight,
            extraLargeHeight: r === u.extraLarge.weight,
            largeHeight: r === u.large.weight,
            mediumHeight: r === u.medium.weight,
            smallHeight: r === u.small.weight,
            extraSmallHeight: r === u.extraSmall.weight,
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
        const m = l.O.client.getSize("rem"),
          E = m.width,
          _ = m.height,
          h = Object.assign({ width: E, height: _ }, d(E, _, s)),
          A = (0, o.createContext)(h),
          p = ["children"];
        const g = (e) => {
          let t = e.children,
            u = (function (e, t) {
              if (null == e) return {};
              var u,
                n,
                r = {},
                o = Object.keys(e);
              for (n = 0; n < o.length; n++) ((u = o[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
              return r;
            })(e, p);
          const n = (0, o.useContext)(A),
            r = n.extraLarge,
            a = n.large,
            l = n.medium,
            s = n.small,
            c = n.extraSmall,
            d = n.extraLargeWidth,
            m = n.largeWidth,
            E = n.mediumWidth,
            _ = n.smallWidth,
            h = n.extraSmallWidth,
            g = n.extraLargeHeight,
            b = n.largeHeight,
            C = n.mediumHeight,
            F = n.smallHeight,
            f = n.extraSmallHeight,
            D = { extraLarge: g, large: b, medium: C, small: F, extraSmall: f };
          if (u.extraLarge || u.large || u.medium || u.small || u.extraSmall) {
            if (u.extraLarge && r) return t;
            if (u.large && a) return t;
            if (u.medium && l) return t;
            if (u.small && s) return t;
            if (u.extraSmall && c) return t;
          } else {
            if (u.extraLargeWidth && d) return i(t, u, D);
            if (u.largeWidth && m) return i(t, u, D);
            if (u.mediumWidth && E) return i(t, u, D);
            if (u.smallWidth && _) return i(t, u, D);
            if (u.extraSmallWidth && h) return i(t, u, D);
            if (!(
              u.extraLargeWidth ||
              u.largeWidth ||
              u.mediumWidth ||
              u.smallWidth ||
              u.extraSmallWidth
            )) {
              if (u.extraLargeHeight && g) return t;
              if (u.largeHeight && b) return t;
              if (u.mediumHeight && C) return t;
              if (u.smallHeight && F) return t;
              if (u.extraSmallHeight && f) return t;
            }
          }
          return null;
        };
        g.defaultProps = {
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
        (0, o.memo)(g);
        const b = (e) => {
            const t = (0, o.useRef)(!1);
            t.current || (e(), (t.current = !0));
          },
          C = (0, o.memo)(({ children: e }) => {
            const t = (0, o.useContext)(A),
              u = (0, o.useState)(t),
              n = u[0],
              r = u[1],
              i = (0, o.useCallback)((e, t) => {
                const u = l.O.view.pxToRem(e),
                  n = l.O.view.pxToRem(t);
                r(Object.assign({ width: u, height: n }, d(u, n, s)));
              }, []);
            (b(() => {
              engine.on("clientResized", i);
            }),
              (0, o.useEffect)(() => () => engine.off("clientResized", i), [i]));
            const c = (0, o.useMemo)(() => Object.assign({}, n), [n]);
            return a().createElement(A.Provider, { value: c }, e);
          });
        var F = u(483),
          f = u.n(F),
          D = u(926),
          v = u.n(D);
        let B, w, S;
        (!(function (e) {
          ((e[(e.ExtraSmall = s.extraSmall.width)] = "ExtraSmall"),
            (e[(e.Small = s.small.width)] = "Small"),
            (e[(e.Medium = s.medium.width)] = "Medium"),
            (e[(e.Large = s.large.width)] = "Large"),
            (e[(e.ExtraLarge = s.extraLarge.width)] = "ExtraLarge"));
        })(B || (B = {})),
          (function (e) {
            ((e[(e.ExtraSmall = s.extraSmall.width)] = "ExtraSmall"),
              (e[(e.Small = s.small.width)] = "Small"),
              (e[(e.Medium = s.medium.width)] = "Medium"),
              (e[(e.Large = s.large.width)] = "Large"),
              (e[(e.ExtraLarge = s.extraLarge.width)] = "ExtraLarge"));
          })(w || (w = {})),
          (function (e) {
            ((e[(e.ExtraSmall = s.extraSmall.height)] = "ExtraSmall"),
              (e[(e.Small = s.small.height)] = "Small"),
              (e[(e.Medium = s.medium.height)] = "Medium"),
              (e[(e.Large = s.large.height)] = "Large"),
              (e[(e.ExtraLarge = s.extraLarge.height)] = "ExtraLarge"));
          })(S || (S = {})));
        const y = () => {
            const e = (0, o.useContext)(A),
              t = e.width,
              u = e.height,
              n = ((e) => {
                switch (!0) {
                  case e.extraLarge:
                    return B.ExtraLarge;
                  case e.large:
                    return B.Large;
                  case e.medium:
                    return B.Medium;
                  case e.small:
                    return B.Small;
                  case e.extraSmall:
                    return B.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), B.ExtraSmall);
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
              a = ((e) => {
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
              mediaSize: n,
              mediaWidth: r,
              mediaHeight: a,
              remScreenWidth: t,
              remScreenHeight: u,
            };
          },
          x = ["children", "className"];
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
        const L = {
            [w.ExtraSmall]: "",
            [w.Small]: v().SMALL_WIDTH,
            [w.Medium]: `${v().SMALL_WIDTH} ${v().MEDIUM_WIDTH}`,
            [w.Large]: `${v().SMALL_WIDTH} ${v().MEDIUM_WIDTH} ${v().LARGE_WIDTH}`,
            [w.ExtraLarge]: `${v().SMALL_WIDTH} ${v().MEDIUM_WIDTH} ${v().LARGE_WIDTH} ${v().EXTRA_LARGE_WIDTH}`,
          },
          M = {
            [S.ExtraSmall]: "",
            [S.Small]: v().SMALL_HEIGHT,
            [S.Medium]: `${v().SMALL_HEIGHT} ${v().MEDIUM_HEIGHT}`,
            [S.Large]: `${v().SMALL_HEIGHT} ${v().MEDIUM_HEIGHT} ${v().LARGE_HEIGHT}`,
            [S.ExtraLarge]: `${v().SMALL_HEIGHT} ${v().MEDIUM_HEIGHT} ${v().LARGE_HEIGHT} ${v().EXTRA_LARGE_HEIGHT}`,
          },
          k = {
            [B.ExtraSmall]: "",
            [B.Small]: v().SMALL,
            [B.Medium]: `${v().SMALL} ${v().MEDIUM}`,
            [B.Large]: `${v().SMALL} ${v().MEDIUM} ${v().LARGE}`,
            [B.ExtraLarge]: `${v().SMALL} ${v().MEDIUM} ${v().LARGE} ${v().EXTRA_LARGE}`,
          },
          N = (e) => {
            let t = e.children,
              u = e.className,
              n = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  r = {},
                  o = Object.keys(e);
                for (n = 0; n < o.length; n++) ((u = o[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
                return r;
              })(e, x);
            const r = y(),
              o = r.mediaWidth,
              i = r.mediaHeight,
              l = r.mediaSize;
            return a().createElement("div", T({ className: f()(u, L[o], M[i], k[l]) }, n), t);
          },
          P = ["children"];
        const O = (e) => {
          let t = e.children,
            u = (function (e, t) {
              if (null == e) return {};
              var u,
                n,
                r = {},
                o = Object.keys(e);
              for (n = 0; n < o.length; n++) ((u = o[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
              return r;
            })(e, P);
          return a().createElement(C, null, a().createElement(N, u, t));
        };
        var H = u(493),
          I = u.n(H);
        function W(e) {
          engine.call("PlaySound", e);
        }
        const X = {
            playHighlight() {
              W("highlight");
            },
            playClick() {
              W("play");
            },
            playYes() {
              W("yes1");
            },
          },
          Y = {
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
        let z, U;
        (!(function (e) {
          ((e.main = "main"),
            (e.primary = "primary"),
            (e.primaryGreen = "primaryGreen"),
            (e.primaryRed = "primaryRed"),
            (e.secondary = "secondary"),
            (e.ghost = "ghost"));
        })(z || (z = {})),
          (function (e) {
            ((e.extraSmall = "extraSmall"), (e.small = "small"), (e.medium = "medium"));
          })(U || (U = {})));
        const G = ({
          children: e,
          size: t,
          isFocused: u,
          type: n,
          disabled: r,
          mixClass: i,
          soundHover: l,
          soundClick: s,
          onMouseEnter: c,
          onMouseMove: d,
          onMouseDown: m,
          onMouseUp: E,
          onMouseLeave: _,
          onClick: h,
        }) => {
          const A = (0, o.useRef)(null),
            p = (0, o.useState)(u),
            g = p[0],
            b = p[1],
            C = (0, o.useState)(!1),
            F = C[0],
            D = C[1],
            v = (0, o.useState)(!1),
            B = v[0],
            w = v[1],
            S = (0, o.useCallback)(() => {
              r || (A.current && (A.current.focus(), b(!0)));
            }, [r]),
            y = (0, o.useCallback)(
              (e) => {
                g && null !== A.current && !A.current.contains(e.target) && b(!1);
              },
              [g],
            ),
            x = (0, o.useCallback)(
              (e) => {
                r || (h && h(e));
              },
              [r, h],
            ),
            T = (0, o.useCallback)(
              (e) => {
                r || (null !== l && W(l), c && c(e), w(!0));
              },
              [r, l, c],
            ),
            L = (0, o.useCallback)(
              (e) => {
                d && d(e);
              },
              [d],
            ),
            M = (0, o.useCallback)(
              (e) => {
                r || (E && E(e), D(!1));
              },
              [r, E],
            ),
            k = (0, o.useCallback)(
              (e) => {
                r || (null !== s && W(s), m && m(e), u && S(), D(!0));
              },
              [r, s, m, S, u],
            ),
            N = (0, o.useCallback)(
              (e) => {
                r || (_ && _(e), D(!1));
              },
              [r, _],
            ),
            P = f()(
              Y.base,
              Y[`base__${n}`],
              {
                [Y.base__disabled]: r,
                [Y[`base__${t}`]]: t,
                [Y.base__focus]: g,
                [Y.base__highlightActive]: F,
                [Y.base__firstHover]: B,
              },
              i,
            ),
            O = f()(Y.state, Y.state__default);
          return (
            (0, o.useEffect)(
              () => (
                document.addEventListener("mousedown", y),
                () => {
                  document.removeEventListener("mousedown", y);
                }
              ),
              [y],
            ),
            (0, o.useEffect)(() => {
              b(u);
            }, [u]),
            a().createElement(
              "div",
              {
                ref: A,
                className: P,
                onMouseEnter: T,
                onMouseMove: L,
                onMouseUp: M,
                onMouseDown: k,
                onMouseLeave: N,
                onClick: x,
              },
              n !== z.ghost &&
                a().createElement(
                  a().Fragment,
                  null,
                  a().createElement("div", { className: Y.back }),
                  a().createElement("span", { className: Y.texture }),
                ),
              a().createElement(
                "span",
                { className: O },
                a().createElement("span", { className: Y.stateDisabled }),
                a().createElement("span", { className: Y.stateHighlightHover }),
                a().createElement("span", { className: Y.stateHighlightActive }),
              ),
              a().createElement(
                "span",
                { className: Y.content, lang: R.strings.settings.LANGUAGE_CODE() },
                e,
              ),
            )
          );
        };
        G.defaultProps = {
          type: z.primary,
          isFocused: !1,
          soundHover: "highlight",
          soundClick: "play",
        };
        const j = (0, o.memo)(G);
        var V = u(364);
        class $ extends a().PureComponent {
          render() {
            let e;
            if ("gold" === this.props.format) e = V.B3.GOLD;
            else e = V.B3.INTEGRAL;
            const t = V.Z5.getNumberFormat(this.props.value, e);
            return void 0 !== this.props.value && void 0 !== t ? t : null;
          }
        }
        $.defaultProps = { format: "integral" };
        const q = (e) => {
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
          },
          K = (e, t, u) => (u < e ? e : u > t ? t : u),
          Q = [];
        function Z(e) {
          const t = (0, o.useRef)(e);
          return (
            (0, o.useLayoutEffect)(() => {
              t.current = e;
            }),
            (0, o.useCallback)((...e) => (0, t.current)(...e), Q)
          );
        }
        function J(e, t, u = []) {
          const n = (0, o.useRef)(0),
            r = (0, o.useCallback)(() => window.clearInterval(n.current), u || []);
          (0, o.useEffect)(() => r, [r]);
          const a = (null != u ? u : []).concat([t]);
          return [
            (0, o.useCallback)((u) => {
              ((n.current = window.setInterval(() => e(u, !0), t)), e(u, !1));
            }, a),
            r,
          ];
        }
        function ee(e, t) {
          var u = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (u) return (u = u.call(e)).next.bind(u);
          if (
            Array.isArray(e) ||
            (u = (function (e, t) {
              if (!e) return;
              if ("string" == typeof e) return te(e, t);
              var u = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === u && e.constructor && (u = e.constructor.name);
              if ("Map" === u || "Set" === u) return Array.from(e);
              if ("Arguments" === u || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(u))
                return te(e, t);
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
        function te(e, t) {
          (null == t || t > e.length) && (t = e.length);
          for (var u = 0, n = new Array(t); u < t; u++) n[u] = e[u];
          return n;
        }
        function ue(e, t, u, n) {
          let r,
            o = !1,
            a = 0;
          function i() {
            r && clearTimeout(r);
          }
          function l(...l) {
            const s = this,
              c = Date.now() - a;
            function d() {
              ((a = Date.now()), u.apply(s, l));
            }
            o ||
              (n && !r && d(),
              i(),
              void 0 === n && c > e
                ? d()
                : !0 !== t &&
                  (r = setTimeout(
                    n
                      ? function () {
                          r = void 0;
                        }
                      : d,
                    void 0 === n ? e - c : e,
                  )));
          }
          return (
            "boolean" != typeof t && ((n = u), (u = t), (t = void 0)),
            (l.cancel = function () {
              (i(), (o = !0));
            }),
            l
          );
        }
        function ne(e, t, u) {
          const n = (0, o.useMemo)(() => ue(u, e), t);
          return ((0, o.useEffect)(() => n.cancel, [n]), n);
        }
        var re = u(30);
        let oe;
        !(function (e) {
          ((e[(e.Next = -1)] = "Next"), (e[(e.Prev = 1)] = "Prev"));
        })(oe || (oe = {}));
        const ae = {
            step: { type: "proportional", factor: 4, clampedArrowStepTimeout: 100 },
            animationConfig: { tension: 170, friction: 26 },
          },
          ie = ({
            getContainerSize: e,
            getBounds: t,
            setScrollPosition: u,
            getDirection: n,
            getWrapperSize: r,
            triggerMouseMoveOnUpdate: a = !1,
          }) => {
            const i = (e, u) => {
              const n = t(e),
                r = n[0],
                o = n[1];
              return K(r, o, u);
            };
            return (s = {}) => {
              const c = s.settings,
                d = void 0 === c ? ae : c,
                m = (0, o.useRef)(null),
                E = (0, o.useRef)(null),
                _ = (() => {
                  const e = (0, o.useMemo)(() => ({}), []),
                    t = (t) => (e[t] || (e[t] = new Map()), e[t]),
                    u = (e, u) => {
                      t(e).set(u, u);
                    },
                    n = (e, u) => {
                      t(e).delete(u);
                    },
                    r = (e, ...u) => {
                      for (var n, r = ee(t(e).values()); !(n = r()).done;) (0, n.value)(...u);
                    };
                  return (0, o.useMemo)(() => ({ on: u, off: n, trigger: r }), []);
                })(),
                h = ne(
                  () => {
                    l.O.view.forceTriggerMouseMove();
                  },
                  [],
                  150,
                ),
                A = (0, re.useSpring)(() => ({
                  scrollPosition: 0,
                  onChange: (e) => {
                    const t = m.current;
                    t && (u(t, e), _.trigger("change", e), a && h());
                  },
                  onRest: (e) => _.trigger("rest", e),
                  onStart: (e) => _.trigger("start", e),
                  onPause: (e) => _.trigger("pause", e),
                })),
                p = A[0],
                g = A[1],
                b = (0, o.useCallback)(
                  (e, t, u) => {
                    var n;
                    const r = p.scrollPosition.get(),
                      o = (null != (n = p.scrollPosition.goal) ? n : 0) - r;
                    return i(e, t * u + o + r);
                  },
                  [p.scrollPosition],
                ),
                C = (0, o.useCallback)(
                  (e, { immediate: t = !1, reset: u = !0 } = {}) => {
                    const n = m.current;
                    n &&
                      g.start({
                        scrollPosition: i(n, e),
                        immediate: t,
                        reset: u,
                        config: d.animationConfig,
                        from: { scrollPosition: i(n, p.scrollPosition.get()) },
                      });
                  },
                  [g, d.animationConfig, p.scrollPosition],
                ),
                F = (0, o.useCallback)(
                  (e) => {
                    const t = m.current,
                      u = E.current;
                    if (!t || !u) return;
                    const n = ((e, t) => {
                        switch (t.type) {
                          case "proportional":
                            return r(e) / t.factor;
                          case "fixed":
                            return t.value;
                        }
                      })(u, d.step),
                      o = b(t, e, n);
                    C(o);
                  },
                  [C, b, d.step],
                ),
                f = (0, o.useCallback)(
                  (e) => {
                    (0 !== e.deltaY && F(n(e)),
                      m.current && _.trigger("mouseWheel", e, p.scrollPosition, t(m.current)));
                  },
                  [p.scrollPosition, F, _],
                ),
                D = ((e, t = []) => {
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
                    q(() => {
                      const e = m.current;
                      e &&
                        (C(i(e, p.scrollPosition.goal), { immediate: !0 }),
                        _.trigger("resizeHandled"));
                    }),
                  [C, p.scrollPosition.goal],
                ),
                v = Z(() => {
                  const e = m.current;
                  if (!e) return;
                  const t = i(e, p.scrollPosition.goal);
                  (t !== p.scrollPosition.goal && C(t, { immediate: !0 }),
                    _.trigger("recalculateContent"));
                });
              (0, o.useEffect)(
                () => (
                  window.addEventListener("resize", D),
                  () => {
                    window.removeEventListener("resize", D);
                  }
                ),
                [D],
              );
              const B = (0, o.useCallback)((e) => _.trigger("isThumbDraggingChanged", e), [_]);
              return (0, o.useMemo)(
                () => ({
                  getWrapperSize: () => (E.current ? r(E.current) : void 0),
                  getContainerSize: () => (m.current ? e(m.current) : void 0),
                  getBounds: () =>
                    m.current
                      ? t(m.current)
                      : (console.warn("getBounds: contentRef.current is null"), [0, 0]),
                  stepTimeout: d.step.clampedArrowStepTimeout,
                  clampPosition: i,
                  handleMouseWheel: f,
                  applyScroll: C,
                  applyStepTo: F,
                  contentRef: m,
                  wrapperRef: E,
                  scrollPosition: g,
                  animationScroll: p,
                  recalculateContent: v,
                  handleIsThumbDragging: B,
                  events: { on: _.on, off: _.off },
                }),
                [p.scrollPosition, C, F, B, _.off, _.on, v, f, g, d.step.clampedArrowStepTimeout],
              );
            };
          },
          le = ie({
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
            getDirection: (e) => (e.deltaY > 1 ? oe.Next : oe.Prev),
            triggerMouseMoveOnUpdate: !0,
          }),
          se = "HorizontalBar_base_49",
          ce = "HorizontalBar_base__nonActive_82",
          de = "HorizontalBar_leftButton_5f",
          me = "HorizontalBar_rightButton_03",
          Ee = "HorizontalBar_track_0d",
          _e = "HorizontalBar_thumb_fd",
          he = "HorizontalBar_rail_32",
          Ae = "disable",
          pe = { pending: !1, offset: 0 },
          ge = (e) => {
            var t;
            return 0.9 * (null != (t = e.getWrapperSize()) ? t : 0);
          },
          be = () => {},
          Ce = (e, t) => Math.max(20, e.offsetWidth * t),
          Fe = (0, o.memo)(
            ({ api: e, classNames: t = {}, getStepByRailClick: u = ge, onDrag: n = be }) => {
              const r = (0, o.useRef)(null),
                i = (0, o.useRef)(null),
                l = (0, o.useRef)(null),
                s = (0, o.useRef)(null),
                c = (0, o.useRef)(null),
                d = e.stepTimeout || 100,
                m = (0, o.useState)(pe),
                E = m[0],
                _ = m[1],
                h = (0, o.useCallback)(
                  (e) => {
                    (_(e),
                      c.current &&
                        n({ type: e.pending ? "dragStart" : "dragEnd", thumb: c.current }));
                  },
                  [n],
                ),
                A = () => {
                  const t = s.current,
                    u = c.current,
                    n = e.getWrapperSize(),
                    r = e.getContainerSize();
                  if (!(n && t && u && r)) return;
                  const o = e.animationScroll.scrollPosition.get(),
                    a = Math.min(1, n / r),
                    d = K(0, 1, o / (r - n)),
                    m = (t.offsetWidth - Ce(t, a)) * d;
                  ((u.style.transform = `translateX(${0 | m}px)`),
                    ((e) => {
                      if (i.current && l.current && s.current && c.current) {
                        if (0 === e)
                          return (i.current.classList.add(Ae), void l.current.classList.remove(Ae));
                        if (
                          ((t = s.current),
                          (u = c.current),
                          e - (t.offsetWidth - u.offsetWidth) >= -0.5)
                        )
                          return (i.current.classList.remove(Ae), void l.current.classList.add(Ae));
                        var t, u;
                        (i.current.classList.remove(Ae), l.current.classList.remove(Ae));
                      }
                    })(m));
                },
                p = Z(() => {
                  ((() => {
                    const t = c.current,
                      u = s.current,
                      n = e.getWrapperSize(),
                      o = e.getContainerSize();
                    if (!(o && t && n && u)) return;
                    const a = Math.min(1, n / o);
                    ((t.style.width = `${Ce(u, a)}px`),
                      (t.style.display = "flex"),
                      r.current &&
                        (1 === a ? r.current.classList.add(ce) : r.current.classList.remove(ce)));
                  })(),
                    A());
                });
              ((0, o.useEffect)(() => q(p)),
                (0, o.useEffect)(
                  () =>
                    q(() => {
                      const t = () => {
                        A();
                      };
                      let u = be;
                      const n = () => {
                        (u(), (u = q(p)));
                      };
                      return (
                        e.events.on("recalculateContent", p),
                        e.events.on("rest", t),
                        e.events.on("change", t),
                        e.events.on("resizeHandled", n),
                        () => {
                          (u(),
                            e.events.off("recalculateContent", p),
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
                      const r = e.contentRef.current;
                      if (!r) return;
                      const o = s.current,
                        a = c.current;
                      if (!r || !o || !a) return;
                      const i = t.screenX - E.offset - o.getBoundingClientRect().x,
                        l = (i / o.offsetWidth) * (null != (u = e.getContainerSize()) ? u : 0);
                      (e.scrollPosition.start({
                        scrollPosition: e.clampPosition(r, l),
                        reset: !0,
                        immediate: !0,
                        from: { scrollPosition: e.animationScroll.scrollPosition.get() },
                      }),
                        n({ type: "dragging", thumb: a, thumbOffset: i, contentOffset: l }));
                    },
                    u = () => {
                      (window.removeEventListener("mousemove", t), h(pe));
                    };
                  return (
                    window.addEventListener("mousemove", t),
                    window.addEventListener("mouseup", u),
                    () => {
                      (window.removeEventListener("mousemove", t),
                        window.removeEventListener("mouseup", u));
                    }
                  );
                }, [e, E.offset, E.pending, n, h]));
              const g = J((t) => e.applyStepTo(t), d, [e]),
                b = g[0],
                C = g[1];
              (0, o.useEffect)(
                () => (
                  document.addEventListener("mouseup", C, !0),
                  () => document.removeEventListener("mouseup", C, !0)
                ),
                [C],
              );
              const F = (e) => {
                e.target.classList.contains(Ae) || W("highlight");
              };
              return a().createElement(
                "div",
                { className: f()(se, t.base), ref: r, onWheel: e.handleMouseWheel },
                a().createElement("div", {
                  className: f()(de, t.leftButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Ae) || 0 !== e.button || (W("play"), b(oe.Next));
                  },
                  onMouseUp: C,
                  ref: i,
                  onMouseEnter: F,
                }),
                a().createElement(
                  "div",
                  {
                    className: f()(Ee, t.track),
                    onMouseDown: (t) => {
                      const n = c.current;
                      if (n && 0 === t.button)
                        if ((W("play"), t.target === n))
                          h({ pending: !0, offset: t.screenX - n.getBoundingClientRect().x });
                        else {
                          ((t) => {
                            const n = c.current,
                              r = e.contentRef.current;
                            if (!n || !r) return;
                            const o = u(e);
                            e.applyScroll(e.animationScroll.scrollPosition.get() + o * t);
                          })(t.screenX > n.getBoundingClientRect().x ? oe.Prev : oe.Next);
                        }
                    },
                    ref: s,
                    onMouseEnter: F,
                  },
                  a().createElement("div", { ref: c, className: f()(_e, t.thumb) }),
                  a().createElement("div", { className: f()(he, t.rail) }),
                ),
                a().createElement("div", {
                  className: f()(me, t.rightButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Ae) || 0 !== e.button || (W("play"), b(oe.Prev));
                  },
                  onMouseUp: C,
                  ref: l,
                  onMouseEnter: F,
                }),
              );
            },
          ),
          fe = {
            base: "HorizontalScroll_base_29",
            wrapper: "HorizontalScroll_wrapper_1e",
            defaultScrollArea: "HorizontalScroll_defaultScrollArea_8d",
          },
          De = ({
            children: e,
            api: t,
            className: u,
            barClassNames: n,
            areaClassName: r,
            classNames: i,
            scrollClassName: l,
            getStepByRailClick: s,
            onDrag: c,
          }) => {
            const d = (0, o.useMemo)(() => {
                const e = n || {};
                return Object.assign({}, e, { base: f()(fe.base, e.base) });
              }, [n]),
              m = (0, o.useMemo)(() => Object.assign({}, t, { handleMouseWheel: () => {} }), [t]);
            return a().createElement(
              "div",
              { className: f()(fe.defaultScroll, u), onWheel: t.handleMouseWheel },
              a().createElement(
                "div",
                { className: f()(fe.defaultScrollArea, r) },
                a().createElement(ve, { className: l, api: m, classNames: i }, e),
              ),
              a().createElement(Fe, { getStepByRailClick: s, api: t, onDrag: c, classNames: d }),
            );
          },
          ve = ({ api: e, className: t, classNames: u, children: n, style: r }) => (
            (0, o.useEffect)(() => q(e.recalculateContent)),
            a().createElement(
              "div",
              { className: f()(fe.base, t), style: r },
              a().createElement(
                "div",
                {
                  className: f()(fe.wrapper, null == u ? void 0 : u.wrapper),
                  onWheel: e.handleMouseWheel,
                  ref: e.wrapperRef,
                },
                a().createElement(
                  "div",
                  { className: f()(fe.content, null == u ? void 0 : u.content), ref: e.contentRef },
                  n,
                ),
              ),
            )
          );
        ((ve.Bar = Fe),
          (ve.Default = De),
          (ve.SeniorityAwards = ({ api: e, className: t, classNames: u, children: n }) => (
            (0, o.useEffect)(() => q(e.recalculateContent)),
            a().createElement(
              "div",
              { className: f()(fe.base, t) },
              a().createElement(
                "div",
                { className: f()(fe.wrapper, null == u ? void 0 : u.wrapper), ref: e.wrapperRef },
                a().createElement(
                  "div",
                  { className: f()(fe.content, null == u ? void 0 : u.content), ref: e.contentRef },
                  n,
                ),
              ),
            )
          )));
        const Be = ie({
            getBounds: (e) => [0, e.scrollHeight - e.offsetHeight],
            getContainerSize: (e) => e.scrollHeight,
            getWrapperSize: (e) => e.offsetHeight,
            setScrollPosition: (e, t) => {
              e.scrollTop = t.value.scrollPosition;
            },
            getDirection: (e) => (e.deltaY > 1 ? oe.Next : oe.Prev),
          }),
          we = "VerticalBar_base_f3",
          Se = "VerticalBar_base__nonActive_42",
          ye = "VerticalBar_topButton_d7",
          xe = "VerticalBar_bottomButton_06",
          Te = "VerticalBar_track_df",
          Le = "VerticalBar_thumb_32",
          Me = "VerticalBar_rail_43",
          Re = "disable",
          ke = () => {},
          Ne = { pending: !1, offset: 0 },
          Pe = (e) => {
            var t;
            return 0.9 * (null != (t = e.getWrapperSize()) ? t : 0);
          },
          Oe = (e, t) => {
            e.contentRef.current && t(e.contentRef.current);
          },
          He = (e, t) => Math.max(20, e.offsetHeight * t),
          Ie = (0, o.memo)(
            ({ api: e, classNames: t = {}, getStepByRailClick: u = Pe, onDrag: n = ke }) => {
              const r = (0, o.useRef)(null),
                i = (0, o.useRef)(null),
                l = (0, o.useRef)(null),
                s = (0, o.useRef)(null),
                c = (0, o.useRef)(null),
                d = e.stepTimeout || 100,
                m = (0, o.useState)(Ne),
                E = m[0],
                _ = m[1],
                h = (0, o.useCallback)(
                  (e) => {
                    (_(e),
                      c.current &&
                        n({ type: e.pending ? "dragStart" : "dragEnd", thumb: c.current }));
                  },
                  [n],
                ),
                A = Z(() => {
                  const t = c.current,
                    u = s.current,
                    n = e.getWrapperSize(),
                    o = e.getContainerSize();
                  if (!(n && o && t && u)) return;
                  const a = Math.min(1, n / o);
                  return (
                    (t.style.height = `${He(u, a)}px`),
                    t.classList.add(Le),
                    r.current &&
                      (1 === a ? r.current.classList.add(Se) : r.current.classList.remove(Se)),
                    a
                  );
                }),
                p = Z(() => {
                  const t = s.current,
                    u = c.current,
                    n = e.getWrapperSize(),
                    r = e.getContainerSize();
                  if (!(n && t && u && r)) return;
                  const o = e.animationScroll.scrollPosition.get(),
                    a = Math.min(1, n / r),
                    d = K(0, 1, o / (r - n)),
                    m = (t.offsetHeight - He(t, a)) * d;
                  ((u.style.transform = `translateY(${0 | m}px)`),
                    ((e) => {
                      if (i.current && l.current && s.current && c.current) {
                        if (0 === e)
                          return (i.current.classList.add(Re), void l.current.classList.remove(Re));
                        if (
                          ((t = s.current),
                          (u = c.current),
                          e - (t.offsetHeight - u.offsetHeight) >= -0.5)
                        )
                          return (i.current.classList.remove(Re), void l.current.classList.add(Re));
                        var t, u;
                        (i.current.classList.remove(Re), l.current.classList.remove(Re));
                      }
                    })(m));
                }),
                g = Z(() => {
                  Oe(e, () => {
                    (A(), p());
                  });
                });
              ((0, o.useEffect)(() => q(g)),
                (0, o.useEffect)(() => {
                  const t = () => {
                    Oe(e, () => {
                      p();
                    });
                  };
                  let u = ke;
                  const n = () => {
                    (u(), (u = q(g)));
                  };
                  return (
                    e.events.on("recalculateContent", g),
                    e.events.on("rest", t),
                    e.events.on("change", t),
                    e.events.on("resizeHandled", n),
                    () => {
                      (u(),
                        e.events.off("recalculateContent", g),
                        e.events.off("rest", t),
                        e.events.off("change", t),
                        e.events.off("resizeHandled", n));
                    }
                  );
                }, [e]),
                (0, o.useEffect)(() => {
                  if (!E.pending) return;
                  const t = (t) => {
                      Oe(e, (u) => {
                        const r = s.current,
                          o = c.current,
                          a = e.getContainerSize();
                        if (!r || !o || !a) return;
                        const i = t.screenY - E.offset - r.getBoundingClientRect().y,
                          l = (i / r.offsetHeight) * a;
                        (e.scrollPosition.start({
                          scrollPosition: e.clampPosition(u, l),
                          reset: !0,
                          immediate: !0,
                          from: { scrollPosition: u.scrollTop },
                        }),
                          n({ type: "dragging", thumb: o, thumbOffset: i, contentOffset: l }));
                      });
                    },
                    u = () => {
                      (window.removeEventListener("mousemove", t),
                        e.handleIsThumbDragging(!1),
                        h(Ne));
                    };
                  return (
                    window.addEventListener("mousemove", t),
                    window.addEventListener("mouseup", u),
                    () => {
                      (window.removeEventListener("mousemove", t),
                        window.removeEventListener("mouseup", u));
                    }
                  );
                }, [e, E.offset, E.pending, n, h]));
              const b = J((t) => e.applyStepTo(t), d, [e]),
                C = b[0],
                F = b[1];
              (0, o.useEffect)(
                () => (
                  document.addEventListener("mouseup", F, !0),
                  () => document.removeEventListener("mouseup", F, !0)
                ),
                [F],
              );
              const D = (e) => {
                e.target.classList.contains(Re) || W("highlight");
              };
              return a().createElement(
                "div",
                { className: f()(we, t.base), ref: r, onWheel: e.handleMouseWheel },
                a().createElement("div", {
                  className: f()(ye, t.topButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Re) || 0 !== e.button || (W("play"), C(oe.Next));
                  },
                  ref: i,
                  onMouseEnter: D,
                }),
                a().createElement(
                  "div",
                  {
                    className: f()(Te, t.track),
                    onMouseDown: (t) => {
                      const n = c.current;
                      if (n && 0 === t.button)
                        if ((W("play"), t.target === n))
                          (e.handleIsThumbDragging(!0),
                            h({ pending: !0, offset: t.screenY - n.getBoundingClientRect().y }));
                        else {
                          ((t) => {
                            c.current &&
                              Oe(e, (n) => {
                                if (!n) return;
                                const r = u(e),
                                  o = e.clampPosition(n, n.scrollTop + r * t);
                                e.applyScroll(o);
                              });
                          })(t.screenY > n.getBoundingClientRect().y ? oe.Prev : oe.Next);
                        }
                    },
                    ref: s,
                    onMouseEnter: D,
                  },
                  a().createElement("div", { ref: c, className: t.thumb }),
                  a().createElement("div", { className: f()(Me, t.rail) }),
                ),
                a().createElement("div", {
                  className: f()(xe, t.bottomButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Re) || 0 !== e.button || (W("play"), C(oe.Prev));
                  },
                  onMouseUp: F,
                  ref: l,
                  onMouseEnter: D,
                }),
              );
            },
          ),
          We = {
            content: "VerticalScroll_content_cb",
            defaultScroll: "VerticalScroll_defaultScroll_f8",
            bar: "VerticalScroll_bar_1e",
            area: "VerticalScroll_area_af",
          },
          Xe = ({
            children: e,
            api: t,
            className: u,
            barClassNames: n,
            areaClassName: r,
            scrollClassName: i,
            scrollClassNames: l,
            getStepByRailClick: s,
            onDrag: c,
          }) => {
            const d = (0, o.useMemo)(() => {
                const e = n || {};
                return Object.assign({}, e, { base: f()(We.base, e.base) });
              }, [n]),
              m = (0, o.useMemo)(() => Object.assign({}, t, { handleMouseWheel: () => {} }), [t]);
            return a().createElement(
              "div",
              { className: f()(We.defaultScroll, u), onWheel: t.handleMouseWheel },
              a().createElement(
                "div",
                { className: f()(We.area, r) },
                a().createElement(Ye, { className: i, classNames: l, api: m }, e),
              ),
              a().createElement(Ie, { getStepByRailClick: s, api: t, onDrag: c, classNames: d }),
            );
          },
          Ye = ({ className: e, classNames: t, children: u, api: n }) => (
            (0, o.useEffect)(() => q(n.recalculateContent)),
            a().createElement(
              "div",
              { className: f()(We.base, e), ref: n.wrapperRef, onWheel: n.handleMouseWheel },
              a().createElement(
                "div",
                { className: f()(We.content, null == t ? void 0 : t.content), ref: n.contentRef },
                u,
              ),
            )
          );
        Ye.Default = Xe;
        const ze = { Vertical: r, Horizontal: n };
        var Ue = u(887),
          Ge = u.n(Ue);
        const je = ["xl", "lg", "md", "sm", "xs"],
          Ve = (e) => e.includes("_") && ((e) => je.includes(e))(e.split("_").at(-1)),
          $e = [B.ExtraLarge, B.Large, B.Medium, B.Small, B.ExtraSmall],
          qe = (e, t) =>
            Object.keys(e).reduce((u, n) => {
              if (n in u) return u;
              if (Ve(n)) {
                const r = n.split("_").slice(0, -1).join("_");
                if (r in u) return u;
                const o = $e.indexOf(t),
                  a = (-1 !== o ? je.slice(o) : [])
                    .map((e) => r + "_" + e)
                    .find((t) => void 0 !== e[t]),
                  i = a ? e[a] : void 0;
                return ((u[r] = void 0 !== i ? i : e[r]), u);
              }
              const r = e[n];
              return (
                void 0 === r ||
                  ((e, t) => je.some((u) => void 0 !== t[`${e}_${u}`]))(n, e) ||
                  (u[n] = r),
                u
              );
            }, {}),
          Ke = (e, t = qe) => {
            const u = (
              (e, t = qe) =>
              (u) => {
                const n = y().mediaSize,
                  r = (0, o.useMemo)(() => t(u, n), [u, n]);
                return a().createElement(e, r);
              }
            )(e, t);
            return a().memo((t) =>
              Object.keys(t).some((e) => Ve(e) && void 0 !== t[e])
                ? a().createElement(u, t)
                : a().createElement(e, t),
            );
          },
          Qe = {
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
          Ze = [
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
        function Je() {
          return (
            (Je =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            Je.apply(this, arguments)
          );
        }
        Object.keys(Ge());
        const et = {
            XL: { mt: Qe.mt__XL, mr: Qe.mr__XL, mb: Qe.mb__XL, ml: Qe.ml__XL },
            LG: { mt: Qe.mt__LG, mr: Qe.mr__LG, mb: Qe.mb__LG, ml: Qe.ml__LG },
            MDp: { mt: Qe.mt__MDp, mr: Qe.mr__MDp, mb: Qe.mb__MDp, ml: Qe.ml__MDp },
            MD: { mt: Qe.mt__MD, mr: Qe.mr__MD, mb: Qe.mb__MD, ml: Qe.ml__MD },
            SMp: { mt: Qe.mt__SMp, mr: Qe.mr__SMp, mb: Qe.mb__SMp, ml: Qe.ml__SMp },
            SM: { mt: Qe.mt__SM, mr: Qe.mr__SM, mb: Qe.mb__SM, ml: Qe.ml__SM },
            XS: { mt: Qe.mt__XS, mr: Qe.mr__XS, mb: Qe.mb__XS, ml: Qe.ml__XS },
          },
          tt = (Object.keys(et), ["mt", "mr", "mb", "ml"]),
          ut = { mt: "marginTop", mr: "marginRight", mb: "marginBottom", ml: "marginLeft" },
          nt = Ke((e) => {
            let t = e.className,
              u = e.width,
              n = e.height,
              r = e.m,
              i = e.mt,
              l = void 0 === i ? r : i,
              s = e.mr,
              c = void 0 === s ? r : s,
              d = e.mb,
              m = void 0 === d ? r : d,
              E = e.ml,
              _ = void 0 === E ? r : E,
              h = e.column,
              A = e.row,
              p = e.flexDirection,
              g = void 0 === p ? (h ? "column" : A && "row") || void 0 : p,
              b = e.flexStart,
              C = e.center,
              F = e.flexEnd,
              D = e.spaceBetween,
              v = e.spaceAround,
              B = e.justifyContent,
              w =
                void 0 === B
                  ? (b ? "flex-start" : C && "center") ||
                    (F && "flex-end") ||
                    (D && "space-between") ||
                    (v && "space-around") ||
                    void 0
                  : B,
              S = e.alignItems,
              y =
                void 0 === S
                  ? (b ? "flex-start" : C && "center") || (F && "flex-end") || void 0
                  : S,
              x = e.alignSelf,
              T = e.wrap,
              L = e.flexWrap,
              M = void 0 === L ? (T ? "wrap" : void 0) : L,
              R = e.grow,
              k = e.shrink,
              N = e.flex,
              P = void 0 === N ? (R || k ? `${R ? 1 : 0} ${k ? 1 : 0} auto` : void 0) : N,
              O = e.style,
              H = e.children,
              I = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  r = {},
                  o = Object.keys(e);
                for (n = 0; n < o.length; n++) ((u = o[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
                return r;
              })(e, Ze);
            const W = (0, o.useMemo)(() => {
                const e = { mt: l, mr: c, mb: m, ml: _ },
                  t = ((e) =>
                    tt.reduce((t, u) => {
                      const n = e[u];
                      return n && "number" != typeof n ? t.concat(et[!0 === n ? "MD" : n][u]) : t;
                    }, []))(e),
                  r = ((e) =>
                    tt.reduce((t, u) => {
                      const n = e[u];
                      return ("number" == typeof n && (t[ut[u]] = n + "rem"), t);
                    }, {}))(e);
                return {
                  computedStyle: Object.assign({}, O, r, {
                    width: void 0 !== u && "number" == typeof u ? u + "rem" : u,
                    height: void 0 !== n && "number" == typeof n ? n + "rem" : n,
                    flex: P,
                    alignSelf: x,
                    display: g || y ? "flex" : void 0,
                    flexDirection: g,
                    flexWrap: M,
                    justifyContent: w,
                    alignItems: y,
                  }),
                  computedClassNames: t,
                };
              }, [u, n, l, c, m, _, O, P, x, g, M, w, y]),
              X = W.computedStyle,
              Y = W.computedClassNames;
            return a().createElement(
              "div",
              Je({ className: f()(Qe.base, ...Y, t), style: X }, I),
              H,
            );
          });
        let rt;
        function ot(e, t) {
          return e.replace(/\{\w+\}/g, (e) => String(t[e.slice(1, -1)]));
        }
        function at(e, t) {
          return e.replace(/(\{|%\()\w+(\}|\)s)/g, (e) => {
            const u = 0 === e.indexOf("%") ? 2 : 1;
            return String(t[e.slice(u, -u)]);
          });
        }
        !(function (e) {
          ((e[(e.left = 0)] = "left"), (e[(e.right = 1)] = "right"));
        })(rt || (rt = {}));
        const it = (e, t, u) => {
            if (u % 2) {
              const u = e.pop();
              return [...e, u + t];
            }
            return [...e, t];
          },
          lt = (e, t, u) => {
            if (0 === u) return [t];
            if (u % 2) return [...e, " " === t ? " " : t];
            {
              const u = e.pop();
              return [...e, u + t];
            }
          },
          st = (e, t, u = rt.left) => e.split(t).reduce(u === rt.left ? it : lt, []),
          ct = (() => {
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
          dt = ["zh_cn", "zh_sg", "zh_tw"],
          mt = (e, t = rt.left) => {
            const u = R.strings.settings.LANGUAGE_CODE().toLowerCase();
            return dt.includes(u)
              ? ct(e)
              : ((e, t = rt.left) => {
                  let u = [];
                  const n =
                      /(?<=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])(\x2D)(?=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])/gu,
                    r = e.replace(/&nbsp;/g, " ");
                  return (st(r, /( )/, t).forEach((e) => (u = u.concat(st(e, n, rt.left)))), u);
                })(e, t);
          },
          Et = "FormatText_base_d0",
          _t = ({ binding: e, text: t = "", classMix: u, alignment: n = rt.left }) =>
            null === t
              ? (console.error("FormatText was supplied with 'null'"), null)
              : a().createElement(
                  o.Fragment,
                  null,
                  t.split("\n").map((t, r) =>
                    a().createElement(
                      "div",
                      { className: f()(Et, u), key: `${t}-${r}` },
                      ((e, t, u) =>
                        e
                          .split(/%\((.*?)\)(?:[sd])?/g)
                          .map((e) => (u && e in u ? u[e] : mt(e, t))))(t, n, e).map((e, t) =>
                        a().createElement(o.Fragment, { key: `${t}-${e}` }, e),
                      ),
                    ),
                  ),
                );
        var ht = u(532),
          At = u.n(ht);
        const pt = {
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
          gt = [
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
        function bt() {
          return (
            (bt =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            bt.apply(this, arguments)
          );
        }
        Object.keys(Ge());
        const Ct = Object.keys(At()),
          Ft = { mt: "MD", mr: "SM", mb: "SM", ml: "SM" },
          ft = { mt: "SM", mr: "XS", mb: "XS", ml: "XS" },
          Dt = { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          vt = {
            XL: { mt: "XL", mr: "XL", mb: "XL", ml: "XL" },
            LG: { mt: "LG", mr: "LG", mb: "LG", ml: "LG" },
            MDp: { mt: "MDp", mr: "MDp", mb: "MDp", ml: "MDp" },
            MD: { mt: "MD", mr: "MD", mb: "MD", ml: "MD" },
            SMp: { mt: "SMp", mr: "SMp", mb: "SMp", ml: "SMp" },
            SM: { mt: "SM", mr: "SM", mb: "SM", ml: "SM" },
            XS: { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          },
          Bt =
            (Object.keys(vt),
            {
              "heading-H144": { mt: "XL", mr: "LG", mb: "LG", ml: "LG" },
              "heading-H73": { mt: "LG", mr: "MD", mb: "MD", ml: "MD" },
              "heading-H56": Ft,
              "heading-H36": Ft,
              "heading-H28": ft,
              "heading-H24": ft,
              "heading-H24R": ft,
              "heading-H22": ft,
              "heading-H20R": ft,
              "heading-H18": ft,
              "heading-H15": Dt,
              "heading-H14": Dt,
              "paragraph-P24": ft,
              "paragraph-P18": ft,
              "paragraph-P16": ft,
              "paragraph-P14": Dt,
              "paragraph-P12": Dt,
              "paragraph-P10": Dt,
            }),
          wt =
            (Object.keys(Bt),
            (e) =>
              e
                ? ((e) => Ct.includes(e))(e)
                  ? { colorClassName: pt[e] }
                  : { colorStyle: { color: e } }
                : {}),
          St = Ke((e) => {
            let t = e.text,
              u = e.variant,
              n = e.className,
              r = e.color,
              i = e.m,
              l = e.mt,
              s = void 0 === l ? i : l,
              c = e.mr,
              d = void 0 === c ? i : c,
              m = e.mb,
              E = void 0 === m ? i : m,
              _ = e.ml,
              h = void 0 === _ ? i : _,
              A = e.style,
              p = e.format,
              g = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  r = {},
                  o = Object.keys(e);
                for (n = 0; n < o.length; n++) ((u = o[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
                return r;
              })(e, gt);
            const b = (0, o.useMemo)(() => {
                const e = wt(r),
                  t = e.colorClassName,
                  u = e.colorStyle,
                  n = void 0 === u ? {} : u;
                return { computedStyle: Object.assign({}, A, n), colorClassName: t };
              }, [A, r]),
              C = b.computedStyle,
              F = b.colorClassName;
            return a().createElement(
              nt,
              bt(
                {
                  className: f()(pt.base, u && pt[u], F, n),
                  style: C,
                  mt: !0 === s ? Bt[u || "paragraph-P16"].mt : s,
                  mr: !0 === d ? Bt[u || "paragraph-P16"].mr : d,
                  mb: !0 === E ? Bt[u || "paragraph-P16"].mb : E,
                  ml: !0 === h ? Bt[u || "paragraph-P16"].ml : h,
                },
                g,
              ),
              void 0 !== p ? a().createElement(_t, bt({}, p, { text: t })) : t,
            );
          }),
          yt = {
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
          xt = [
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
        function Tt() {
          return (
            (Tt =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            Tt.apply(this, arguments)
          );
        }
        class Lt extends a().PureComponent {
          constructor(...e) {
            (super(...e),
              (this.state = { hover: !1, click: !1 }),
              (this._onMouseEnter = (e) => (t) => {
                (e && e(t),
                  this.setState({ hover: !0 }),
                  this.props.soundHover && W(this.props.soundHover));
              }),
              (this._onMouseLeave = (e) => (t) => {
                (e && e(t), this.setState({ hover: !1, click: !1 }));
              }),
              (this._onMouseDown = (e) => (t) => {
                (e && e(t),
                  this.setState({ click: !0 }),
                  this.props.soundClick && W(this.props.soundClick));
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
              r = e.side,
              o = e.type,
              i = e.classNames,
              l = e.onMouseEnter,
              s = e.onMouseLeave,
              c = e.onMouseDown,
              d = e.onMouseUp,
              m =
                (e.soundClick,
                e.soundHover,
                (function (e, t) {
                  if (null == e) return {};
                  var u,
                    n,
                    r = {},
                    o = Object.keys(e);
                  for (n = 0; n < o.length; n++) ((u = o[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
                  return r;
                })(e, xt)),
              E = f()(yt.base, yt[`base__${o}`], yt[`base__${r}`], null == i ? void 0 : i.base),
              _ = f()(yt.icon, yt[`icon__${o}`], yt[`icon__${r}`], null == i ? void 0 : i.icon),
              h = f()(yt.glow, null == i ? void 0 : i.glow),
              A = f()(yt.caption, yt[`caption__${o}`], null == i ? void 0 : i.caption),
              p = f()(yt.goto, null == i ? void 0 : i.goto);
            return a().createElement(
              "div",
              Tt(
                {
                  className: E,
                  onMouseEnter: this._onMouseEnter(l),
                  onMouseLeave: this._onMouseLeave(s),
                  onMouseDown: this._onMouseDown(c),
                  onMouseUp: this._onMouseUp(d),
                  onFocus: this.handleFocus,
                  onBlur: this.handleBlur,
                  onClick: u,
                },
                m,
              ),
              "info" !== o && a().createElement("div", { className: yt.shine }),
              a().createElement(
                "div",
                { className: _ },
                a().createElement("div", { className: h }),
              ),
              a().createElement("div", { className: A }, t),
              n && a().createElement("div", { className: p }, n),
            );
          }
        }
        Lt.defaultProps = {
          side: "left",
          type: "back",
          soundHover: "highlight",
          soundClick: "play",
        };
        const Mt = [
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
        function Rt(e) {
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
        const kt = (e, t, u = {}, n = 0) => {
            viewEnv.handleViewEvent(
              Object.assign(
                {
                  __Type: "GFViewEventProxy",
                  type: V.B0.TOOLTIP,
                  contentID: e,
                  decoratorID: t,
                  targetID: n,
                },
                u,
              ),
            );
          },
          Nt = (e) => {
            let t = e.children,
              u = e.contentId,
              n = e.args,
              r = e.onMouseEnter,
              a = e.onMouseLeave,
              i = e.onMouseDown,
              l = e.onClick,
              s = e.ignoreShowDelay,
              c = void 0 !== s && s,
              d = e.ignoreMouseClick,
              m = void 0 !== d && d,
              E = e.decoratorId,
              _ = void 0 === E ? 0 : E,
              h = e.isEnabled,
              A = void 0 === h || h,
              p = e.targetId,
              g = void 0 === p ? 0 : p,
              b = e.onShow,
              C = e.onHide,
              F = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  r = {},
                  o = Object.keys(e);
                for (n = 0; n < o.length; n++) ((u = o[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
                return r;
              })(e, Mt);
            const f = (0, o.useRef)({
                timeoutId: 0,
                isVisible: !1,
                prevTarget: null,
                hideTimerId: null,
              }),
              D = (0, o.useMemo)(
                () =>
                  g ||
                  ((e = 1) => {
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
                  })().resId,
                [g],
              ),
              v = (0, o.useCallback)(() => {
                (f.current.isVisible && f.current.timeoutId) ||
                  (kt(u, _, { isMouseEvent: !0, on: !0, arguments: Rt(n) }, D),
                  b && b(),
                  (f.current.isVisible = !0));
              }, [u, _, n, D, b]),
              B = (0, o.useCallback)(() => {
                if (f.current.isVisible || f.current.timeoutId) {
                  const e = f.current.timeoutId;
                  (e > 0 && (clearTimeout(e), (f.current.timeoutId = 0)),
                    kt(u, _, { on: !1 }, D),
                    f.current.isVisible && C && C(),
                    (f.current.isVisible = !1));
                }
              }, [u, _, D, C]),
              w = (0, o.useCallback)((e) => {
                f.current.isVisible &&
                  ((f.current.prevTarget = document.elementFromPoint(e.clientX, e.clientY)),
                  (f.current.hideTimerId = window.setTimeout(() => {
                    const t = document.elementFromPoint(e.clientX, e.clientY);
                    t && !t.isSameNode(f.current.prevTarget) && B();
                  }, 200)));
              }, []);
            ((0, o.useEffect)(() => {
              const e = f.current.hideTimerId;
              return (
                document.addEventListener("wheel", w, { capture: !0 }),
                () => {
                  (document.removeEventListener("wheel", w, { capture: !0 }),
                    e && window.clearTimeout(e));
                }
              );
            }, []),
              (0, o.useEffect)(() => {
                !1 === A && B();
              }, [A, B]),
              (0, o.useEffect)(
                () => (
                  window.addEventListener("mouseleave", B),
                  () => {
                    (window.removeEventListener("mouseleave", B), B());
                  }
                ),
                [B],
              ));
            return A
              ? (0, o.cloneElement)(
                  t,
                  Object.assign(
                    {
                      onMouseEnter:
                        ((S = t.props.onMouseEnter),
                        (e) => {
                          (e.clientX === window.innerWidth && e.clientY === window.innerHeight) ||
                            ((f.current.timeoutId = window.setTimeout(v, c ? 100 : 400)),
                            r && r(e),
                            S && S(e));
                        }),
                      onMouseLeave: ((e) => (t) => {
                        (B(), null == a || a(t), null == e || e(t));
                      })(t.props.onMouseLeave),
                      onClick: ((e) => (t) => {
                        (!1 === m && B(), null == l || l(t), null == e || e(t));
                      })(t.props.onClick),
                      onMouseDown: ((e) => (t) => {
                        (!1 === m && B(), null == i || i(t), null == e || e(t));
                      })(t.props.onMouseDown),
                    },
                    F,
                  ),
                )
              : t;
            var S;
          };
        var Pt = u(521);
        const Ot = (e) => {
          console.error(e.type + ": useKeydownListener hook :: Callback is not defined");
        };
        function Ht(e = Pt.n.NONE, t = Ot, u = !1) {
          (0, o.useEffect)(() => {
            if (e !== Pt.n.NONE)
              return (
                window.addEventListener("keydown", n, u),
                () => {
                  window.removeEventListener("keydown", n, u);
                }
              );
            function n(n) {
              if (n.keyCode === e) {
                if (l.O.view.isEventHandled()) return;
                (l.O.view.setEventHandled(), t(n), u && n.stopPropagation());
              }
            }
          }, [t, e, u]);
        }
        function It({
          key: e = Pt.n.ESCAPE,
          callback: t = () => l.O.view.sendEvent.close(),
          preventPropagation: u = !0,
        } = {}) {
          return (Ht(e, t, u), t);
        }
        const Wt = (e, t) => {
          (0, o.useEffect)(() => {
            let t = null;
            return (
              (t = requestAnimationFrame(() => {
                t = requestAnimationFrame(() => {
                  ((t = null), e());
                });
              })),
              () => {
                null !== t && cancelAnimationFrame(t);
              }
            );
          }, t);
        };
        var Xt = u(515);
        const Yt = ["children", "body", "header", "note", "alert", "args"];
        function zt() {
          return (
            (zt =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            zt.apply(this, arguments)
          );
        }
        const Ut = R.views.common.tooltip_window.simple_tooltip_content,
          Gt = (e) => {
            let t = e.children,
              u = e.body,
              n = e.header,
              r = e.note,
              i = e.alert,
              l = e.args,
              s = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  r = {},
                  o = Object.keys(e);
                for (n = 0; n < o.length; n++) ((u = o[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
                return r;
              })(e, Yt);
            const c = (0, o.useMemo)(() => {
              const e = Object.assign({}, l, { body: u, header: n, note: r, alert: i });
              for (const t in e) void 0 === e[t] && delete e[t];
              return e;
            }, [i, u, n, r, l]);
            return a().createElement(
              Nt,
              zt(
                {
                  contentId:
                    ((d = null == l ? void 0 : l.hasHtmlContent),
                    d ? Ut.SimpleTooltipHtmlContent("resId") : Ut.SimpleTooltipContent("resId")),
                  decoratorId: R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
                  args: c,
                },
                s,
              ),
              t,
            );
            var d;
          },
          jt = "WarningText_base_5d",
          Vt = "WarningText_header_57",
          $t = "WarningText_headerIcon_2f",
          qt = "WarningText_description_78",
          Kt = a().memo(({ header: e, description: t }) =>
            a().createElement(
              "div",
              { className: jt },
              a().createElement(
                "div",
                { className: Vt },
                a().createElement("div", { className: $t }),
                e,
              ),
              a().createElement("div", { className: qt }, t),
            ),
          ),
          Qt = "ListEmptyState_base_5f",
          Zt = "ListEmptyState_content_22",
          Jt = "ListEmptyState_buttonWrapper_fa",
          eu = "ListEmptyState_button_cd",
          tu = R.strings.customization,
          uu = (0, o.memo)(
            ({
              warningHeader: e,
              warningDescription: t,
              buttonType: u = z.secondary,
              tooltipArgs: n = { body: tu.customization.resetFilter.tooltip.text() },
              className: r,
              onClick: o,
              children: i,
            }) =>
              a().createElement(
                "div",
                { className: f()(Qt, r) },
                a().createElement(
                  "div",
                  { className: Zt },
                  a().createElement(Kt, { header: e, description: t }),
                  i &&
                    a().createElement(
                      "div",
                      { className: Jt },
                      a().createElement(
                        Gt,
                        n,
                        a().createElement(
                          j,
                          { size: U.small, type: u, onClick: o, mixClass: eu },
                          i,
                        ),
                      ),
                    ),
                ),
              ),
          ),
          nu = ["children"];
        function ru() {
          return (
            (ru =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            ru.apply(this, arguments)
          );
        }
        const ou = (e) => {
          let t = e.children,
            u = (function (e, t) {
              if (null == e) return {};
              var u,
                n,
                r = {},
                o = Object.keys(e);
              for (n = 0; n < o.length; n++) ((u = o[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
              return r;
            })(e, nu);
          return a().createElement(
            Nt,
            ru(
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
        V.Sw.instance;
        let au;
        !(function (e) {
          ((e.None = "None"), (e.Shallow = "Shallow"), (e.Deep = "Deep"));
        })(au || (au = {}));
        (0, o.createContext)("model");
        const iu = (e) => {
            if (!e) return !1;
            const t = e.getBoundingClientRect(),
              u = t.width,
              n = t.height;
            return 0 !== u && 0 !== n;
          },
          lu = (e) => {
            const t = (0, o.useState)(iu(e ? e.current : null)),
              u = t[0],
              n = t[1];
            return (
              (0, o.useEffect)(() => {
                let t = 0;
                const u = () => {
                  t = requestAnimationFrame(() => {
                    iu(e ? e.current : null) ? n(!0) : u();
                  });
                };
                return (
                  u(),
                  () => {
                    cancelAnimationFrame(t);
                  }
                );
              }, [e]),
              (0, o.useEffect)(() => () => n(!1), [e]),
              u
            );
          };
        var su = u(380),
          cu = u.n(su);
        const du = "ScrollArea_base_47",
          mu = "ScrollArea_base__scrollIndent_1d",
          Eu = "ScrollArea_base__verticalScrollbarMargin_50",
          _u = "ScrollArea_base__multiple_44",
          hu = "ScrollArea_base__hidden_ec";
        a().forwardRef((e, t) => {
          const u = e.offsetLeft,
            n = void 0 === u ? 0 : u,
            r = e.offsetTop,
            i = void 0 === r ? 0 : r,
            l = e.scrollSettings,
            s = e.onUpdateActiveAxis,
            c = e.onHorizontalScroll,
            d = e.onVerticalScroll,
            m = e.onOverScrollAtBeginning,
            E = e.onOverScrollAtEnd,
            _ = e.wrapperIndent,
            h = e.verticalScrollbarMargin,
            A = e.isMultipleScroll,
            p = e.scrollAreaContainer,
            g = e.children,
            b = e.classMix,
            C = e.onScrollLeftHandled,
            F = (0, o.useState)(!1),
            D = F[0],
            v = F[1],
            B = (0, o.useState)(),
            w = B[0],
            S = B[1],
            y = (0, o.useState)(),
            x = y[0],
            T = y[1],
            L = (0, o.useRef)(null),
            M = (0, o.useCallback)(() => {
              w &&
                s &&
                s({ x: w.scrollbarXActive, y: w.scrollbarYActive }, { x: w.reach.x, y: w.reach.y });
            }, [s, w]),
            R = (0, o.useCallback)(() => w, [w]),
            k = (0, o.useCallback)(() => {
              w && w.update();
            }, [w]),
            N = (0, o.useCallback)(
              (e, t, u) => {
                w && (w.setScrollLeft(e, t, u), C && C(e, w.contentWidth - w.containerWidth));
              },
              [w, C],
            ),
            P = (0, o.useCallback)(
              (e) => {
                w && (w.setScrollLeftImmediately(e), C && C(e, w.contentWidth - w.containerWidth));
              },
              [w, C],
            ),
            O = (0, o.useCallback)(
              (e, t, u) => {
                w && w.setScrollTop(e, t, u);
              },
              [w],
            ),
            H = (0, o.useCallback)(
              (e) => {
                w && w.setScrollTopImmediately(e);
              },
              [w],
            ),
            I = (0, o.useCallback)(() => {
              if (x && c && w) {
                const e = { scrollPosition: x.scrollLeft < 0 ? 0 : x.scrollLeft, reach: w.reach.x };
                c(e);
              }
            }, [c, x, w]),
            W = (0, o.useCallback)(() => {
              if (x && d && w) {
                const e = { scrollPosition: x.scrollTop, reach: w.reach.y };
                d(e);
              }
            }, [d, x, w]),
            X = (0, o.useCallback)(() => {
              m && m();
            }, [m]),
            Y = (0, o.useCallback)(() => {
              E && E();
            }, [E]),
            z = (0, o.useCallback)(
              (e) => {
                ("function" == typeof t ? t(e) : null !== t && (t.current = e), T(e));
              },
              [t],
            ),
            U = (0, o.useCallback)(() => {
              w &&
                (w.update(),
                (L.current = q(() => {
                  M();
                })));
            }, [w, M]),
            G = (0, o.useCallback)((e) => {
              0 === e.screenX &&
                0 === e.screenY &&
                (e.stopImmediatePropagation(), e.preventDefault());
            }, []);
          (0, o.useEffect)(() => {
            if (w && x)
              return (
                document.addEventListener("mousemove", G),
                window.addEventListener("resize", U),
                x.addEventListener("ps-scroll-x", I),
                x.addEventListener("ps-scroll-y", W),
                x.addEventListener("over-scroll-beginning", X),
                x.addEventListener("over-scroll-ending", Y),
                v(!0),
                () => {
                  (window.removeEventListener("resize", U),
                    document.removeEventListener("mousemove", G),
                    x &&
                      (x.removeEventListener("ps-scroll-x", I),
                      x.removeEventListener("ps-scroll-y", W),
                      x.removeEventListener("over-scroll-beginning", X),
                      x.removeEventListener("over-scroll-ending", Y)));
                }
              );
          }, [G, I, X, Y, U, x, w, W]);
          const j = (0, o.useRef)(x || null);
          j.current = x || null;
          const V = lu(j);
          ((0, o.useEffect)(
            () => (
              !w && x && V && S(new (cu())(x, Object.assign({}, l))),
              () => {
                w && (w.destroy(), S(void 0));
              }
            ),
            [x, V, l, w],
          ),
            (0, o.useEffect)(
              () => () => {
                null == L.current || L.current();
              },
              [],
            ),
            (0, o.useEffect)(
              () =>
                q(() => {
                  w && M();
                }),
              [M, w],
            ),
            (0, o.useEffect)(() => {
              n > 0 && P(n);
            }, [n, P]),
            (0, o.useEffect)(() => {
              i > 0 && H(i);
            }, [i, H]),
            (0, o.useEffect)(() => {
              p &&
                ((p.setScrollLeft = N),
                (p.setScrollTop = O),
                (p.setScrollLeftImmediately = P),
                (p.setScrollTopImmediately = H),
                (p.updateScrollArea = k),
                (p.getScrollbar = R));
            }, [p, N, P, O, H, k, R]));
          const $ = f()(du, { [mu]: _, [hu]: !D, [Eu]: h, [_u]: A }, b);
          return a().createElement("div", { className: $, ref: z }, g);
        });
        let Au;
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
        })(Au || (Au = {}));
        Date.now();
        V.Sw.instance;
        let pu, gu, bu, Cu, Fu, fu, Du, vu, Bu;
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
            (e.Entitlements = "entitlements"),
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
            (e.NyPetGoodies = "nyPetGoodies"),
            (e.HiddenVehicle = "hidden_vehicle"),
            (e.NyStaticDogTag = "nyStaticDogTag"),
            (e.NyToys = "nyToys"),
            (e.NyLootboxFragment = "nyLootboxFragment"));
        })(pu || (pu = {})),
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
          })(gu || (gu = {})),
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
          })(bu || (bu = {})),
          (function (e) {
            ((e.MULTI = "multi"),
              (e.CURRENCY = "currency"),
              (e.PREMIUM_PLUS = "premium_plus"),
              (e.NUMBER = "number"),
              (e.STRING = "string"));
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
            e.BATTLE_BOOSTER = "battleBooster";
          })(fu || (fu = {})),
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
          })(Du || (Du = {})),
          (function (e) {
            ((e.Small = "400x300"), (e.Big = "600x450"));
          })(vu || (vu = {})),
          (function (e) {
            e.ProgressionStyle = "progressionStyle";
          })(Bu || (Bu = {})));
        let wu;
        !(function (e) {
          ((e.Plus = "plus"), (e.Minus = "minus"));
        })(wu || (wu = {}));
        var Su;
        !(function (e) {
          ((e.None = ""),
            (e.Trophy = "trophy"),
            (e.Deluxe = "delux"),
            (e.Modernized = "modernized"));
        })(Su || (Su = {}));
        R.strings.selectable_reward.reward;
        R.strings.selectable_reward.tabs;
        let yu;
        !(function (e) {
          ((e[(e.None = 0)] = "None"), (e[(e.Accepting = 1)] = "Accepting"));
        })(yu || (yu = {}));
        const xu = (0, o.createContext)(yu.None),
          Tu = {
            base: "Card_base_be",
            base__selected: "Card_base__selected_ae",
            base__disabled: "Card_base__disabled_cc",
            base__addDisabled: "Card_base__addDisabled_f0",
            optDeviceType: "Card_optDeviceType_6e",
            holder: "Card_holder_25",
            image: "Card_image_89",
            packSize: "Card_packSize_1f",
            label: "Card_label_19",
            cardRightTop: "Card_cardRightTop_dd",
            cardLeftTop: "Card_cardLeftTop_7e",
            storage: "Card_storage_19",
            storage__zero: "Card_storage__zero_d0",
            storage__hidden: "Card_storage__hidden_5c",
            storageIcon: "Card_storageIcon_99",
            onTank: "Card_onTank_b6",
            onTank__hidden: "Card_onTank__hidden_0b",
            onTankIcon: "Card_onTankIcon_c6",
            countText: "Card_countText_e5",
            select: "Card_select_c4",
            state: "Card_state_ac",
            stateText: "Card_stateText_4b",
            stateIcon: "Card_stateIcon_b0",
            glow: "Card_glow_2e",
            base__stateReceived: "Card_base__stateReceived_b8",
            currencyHolder: "Card_currencyHolder_22",
            exchangePrice: "Card_exchangePrice_40",
            paintsIcon: "Card_paintsIcon_83",
            disabled: "Card_disabled_ec",
            blink: "Card_blink_66",
          },
          Lu = "Image_base_46",
          Mu = "Image_shine_7a",
          Ru = "Image_content_9b",
          ku = (0, o.memo)(({ isDim: e, icon: t }) => {
            t = t.replace("..", "img://gui");
            const u = (0, o.useMemo)(() => ({ backgroundImage: `url(${t})` }), [t]);
            return t
              ? a().createElement(
                  "div",
                  { className: Lu },
                  e && a().createElement("div", { className: Mu }),
                  a().createElement("div", { className: Ru, style: u }),
                )
              : a().createElement("div", { className: Ru });
          }),
          Nu = {
            base: "SelectButton_base_46",
            base__plus: "SelectButton_base__plus_0a",
            base__disabled: "SelectButton_base__disabled_12",
            base__minus: "SelectButton_base__minus_3c",
          };
        let Pu;
        !(function (e) {
          ((e.Plus = "plus"), (e.Minus = "minus"));
        })(Pu || (Pu = {}));
        const Ou = R.strings.event.customizationResource.card,
          Hu = a().memo(
            ({
              type: e = Pu.Plus,
              isEnabled: t,
              onClick: u,
              onMouseEnter: n,
              isLimitReached: r,
              limit: i,
            }) => {
              const l = r && e === Pu.Plus,
                s = (0, o.useCallback)(
                  (e) => {
                    (e.stopPropagation(), t && !l && u(e));
                  },
                  [t, l, u],
                ),
                c = f()(Nu.base, Nu[`base__${e}`], (!t || l) && Nu.base__disabled);
              return a().createElement(
                Gt,
                {
                  header: t
                    ? Ou.tooltips.isLimitReached.header()
                    : Ou.tooltips.maxSelected.header(),
                  body: t
                    ? ot(Ou.tooltips.isLimitReached.body(), { limit: i })
                    : Ou.tooltips.maxSelected.body(),
                  isEnabled: l || (!t && e === Pu.Plus),
                },
                a().createElement("div", { className: c, onMouseEnter: n, onClick: s }),
              );
            },
          ),
          Iu = R.strings.event.customizationResource.card,
          Wu = a().memo(
            ({
              intCD: e,
              vehicleCD: t,
              onAdd: u,
              onReduce: n,
              selectedCount: r,
              installedCount: i,
              inventoryCount: l,
              availableCount: s,
              icon: c,
              name: d,
              exchangePrice: m,
              isFilled: E,
              tooltip: _,
              isLimitReached: h,
              limit: A,
            }) => {
              const p = r > 0,
                g = (0, o.useContext)(xu) === yu.Accepting && p,
                b = s > r,
                C = 0 === s || (h && 0 === r),
                F = d,
                D = (0, o.useCallback)(() => {
                  !b || C || h || (W(R.sounds.bp_click_plus()), u(e, t));
                }, [b, C, h, u, e, t]),
                v = (0, o.useCallback)(() => {
                  (W(R.sounds.bp_click_plus()), u(e, t));
                }, [e, t, u]),
                B = (0, o.useCallback)(() => {
                  (W(R.sounds.bp_click_minus()), n(e, t));
                }, [e, t, n]),
                w = (0, o.useCallback)(() => {
                  W("bp_highlight");
                }, []),
                S = (0, o.useCallback)(() => {
                  W(R.sounds.highlight());
                }, []),
                y = f()(
                  Tu.base,
                  p && Tu.base__selected,
                  g && Tu.base__accepting,
                  C && Tu.base__disabled,
                  !b && Tu.base__addDisabled,
                ),
                x = f()(Tu.storage, l <= 0 && Tu.storage__hidden, s === r && Tu.storage__zero),
                T = f()(Tu.onTank, i <= 0 && Tu.onTank__hidden),
                L = (0, o.useMemo)(
                  () => ({ intCD: e, tooltip: _, showInventoryBlock: s > 0, progressionLevel: -1 }),
                  [e, s, _],
                );
              return a().createElement(
                ou,
                { args: L },
                a().createElement(
                  "div",
                  { className: y, onClick: D, onMouseEnter: w },
                  E &&
                    a().createElement(
                      a().Fragment,
                      null,
                      a().createElement(
                        "div",
                        { className: Tu.cardRightTop },
                        a().createElement(
                          "div",
                          { className: x },
                          a().createElement("div", { className: Tu.storageIcon }),
                          l - r,
                        ),
                        a().createElement(
                          "div",
                          { className: T },
                          a().createElement("div", { className: Tu.onTankIcon }),
                          i,
                        ),
                      ),
                      a().createElement(
                        "div",
                        { className: Tu.cardLeftTop },
                        a().createElement(
                          Nt,
                          {
                            contentId:
                              R.views.lobby.customization_resource.tooltips.CustomizationResourceCurrencyTooltipView(
                                "resId",
                              ),
                          },
                          a().createElement(
                            "div",
                            { className: Tu.currencyHolder },
                            a().createElement(
                              "div",
                              { className: Tu.exchangePrice },
                              a().createElement($, { value: m }),
                            ),
                            a().createElement("div", { className: Tu.paintsIcon }),
                          ),
                        ),
                      ),
                      a().createElement(
                        "div",
                        { className: Tu.holder },
                        a().createElement(
                          "div",
                          { className: Tu.image },
                          a().createElement(ku, { isDim: !1, icon: c }),
                        ),
                        C && a().createElement("div", { className: Tu.disabled }),
                        r > 1 &&
                          a().createElement(
                            "div",
                            { className: Tu.packSize },
                            at(Iu.selectedCount(), { packSize: r }),
                          ),
                      ),
                      a().createElement("div", { className: Tu.label }, F),
                      C
                        ? a().createElement(
                            "div",
                            { className: Tu.state },
                            a().createElement(
                              "div",
                              { className: Tu.stateText },
                              b ? Iu.limitReached() : Iu.warning(),
                            ),
                            a().createElement("div", { className: Tu.stateIcon }),
                          )
                        : a().createElement(
                            a().Fragment,
                            null,
                            a().createElement("div", { className: Tu.countText }, r),
                            a().createElement(
                              "div",
                              { className: Tu.select },
                              a().createElement(Hu, {
                                type: Pu.Minus,
                                isEnabled: p,
                                onClick: B,
                                onMouseEnter: S,
                              }),
                              a().createElement(Hu, {
                                type: Pu.Plus,
                                isEnabled: b,
                                isLimitReached: h,
                                limit: A,
                                onClick: v,
                                onMouseEnter: S,
                              }),
                            ),
                          ),
                      a().createElement("div", { className: Tu.glow }),
                    ),
                ),
              );
            },
          ),
          Xu = "Category_base_e3",
          Yu = "Category_base__viewReady_8d",
          zu = "Category_base__selected_6a",
          Uu = "Category_glow_3f",
          Gu = "Category_title_24",
          ju = "Category_imageContainer_aa",
          Vu = "Category_image_8e",
          $u = "Category_base__completed_8c",
          qu = "Category_base__accepting_b0",
          Ku = "Category_check_a2",
          Qu = "Category_counter_21",
          Zu = R.strings.event.customizationResource.tabs,
          Ju = (e, t = bu.Small) => `R.images.gui.maps.icons.quests.bonuses.${t}.${e}`;
        var en;
        !(function (e) {
          ((e[(e.None = 0)] = "None"), (e[(e.Accepting = 1)] = "Accepting"));
        })(en || (en = {}));
        const tn = (0, o.createContext)(en.None),
          un = a().memo(
            ({
              itemType: e,
              selectedCount: t,
              availableCount: u,
              isSelected: n,
              onClick: r,
              tabId: i,
            }) => {
              const l = (0, o.useContext)(tn),
                s = y().mediaSize,
                c = t === u,
                d = l === en.Accepting && t > 0 && !n,
                m = s >= B.Medium ? bu.Big : bu.Small,
                E = (0, o.useState)(!1),
                _ = E[0],
                h = E[1],
                A = (0, o.useMemo)(() => ({ backgroundImage: `url(${Ju(e, m)})` }), [m, e]),
                p = (0, o.useMemo)(
                  () => at(Zu.counter(), { selectedCount: t, availableCount: u }),
                  [t, u],
                ),
                g = (0, o.useCallback)(() => {
                  W("bp_highlight");
                }, []);
              (0, o.useEffect)(
                () =>
                  q(() => {
                    h(!0);
                  }),
                [],
              );
              const b = f()(Xu, _ && Yu, c && $u, n && zu, d && qu);
              return a().createElement(
                Nt,
                {
                  contentId:
                    R.views.lobby.customization_resource.tooltips.CategoryTooltipView("resId"),
                  args: { tabId: i },
                },
                a().createElement(
                  "div",
                  {
                    className: b,
                    onClick: () => {
                      r(i);
                    },
                    onMouseEnter: g,
                  },
                  a().createElement("div", { className: Uu }),
                  a().createElement(
                    "div",
                    { className: Gu },
                    ((C = e), R.strings.event.customizationResource.tabs.items.$dyn(C)),
                  ),
                  a().createElement(
                    "div",
                    { className: ju },
                    a().createElement("div", { className: Vu, style: A }),
                    a().createElement("div", { className: Ku }),
                  ),
                  a().createElement("div", { className: Qu }, p),
                ),
              );
              var C;
            },
          );
        function nn() {
          return !1;
        }
        console.log;
        var rn = u(174);
        function on(e, t) {
          var u = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (u) return (u = u.call(e)).next.bind(u);
          if (
            Array.isArray(e) ||
            (u = (function (e, t) {
              if (!e) return;
              if ("string" == typeof e) return an(e, t);
              var u = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === u && e.constructor && (u = e.constructor.name);
              if ("Map" === u || "Set" === u) return Array.from(e);
              if ("Arguments" === u || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(u))
                return an(e, t);
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
        function an(e, t) {
          (null == t || t > e.length) && (t = e.length);
          for (var u = 0, n = new Array(t); u < t; u++) n[u] = e[u];
          return n;
        }
        const ln = (e) => (0 === e ? window : window.subViews.get(e));
        function sn(e) {
          var t;
          return e && "value" in e && null != (t = e.constructor) && t.name.includes("ArrayItem")
            ? null == e
              ? void 0
              : e.value
            : e;
        }
        function cn(e, t) {
          for (let u = 0; u < e.length; u++) {
            const n = sn(e[u]);
            if (t(n, u, e)) return n;
          }
        }
        const dn = (e) => {
            return null !== e && "object" == typeof e
              ? "CoherentArrayProxy" === e.constructor.name
                ? ((t = e),
                  (u = (e) => ("object" == typeof e ? dn(e) : e)),
                  Array.isArray(t)
                    ? t.map(u)
                    : t.map((e, t, n) => u(null == e ? void 0 : e.value, t, n)))
                : Array.isArray(e)
                  ? e.map((e) => ("object" == typeof e ? dn(e) : e))
                  : Object.fromEntries(
                      Object.entries(e).map(([e, t]) => [e, "object" == typeof t ? dn(t) : t]),
                    )
              : e;
            var t, u;
          },
          mn = (e) => dn(e);
        var En = u(946);
        const _n = ((e, t) => {
            const u = (0, o.createContext)({});
            return [
              function ({ mode: n = "real", options: r, children: i, mocks: s }) {
                const c = (0, o.useRef)([]),
                  d = (u, n, r) => {
                    var o;
                    const a = (function ({
                        initializer: e = !0,
                        rootId: t = 0,
                        getRoot: u = ln,
                        context: n = "model",
                      } = {}) {
                        const r = new Map();
                        function o(e, t = 0) {
                          viewEnv.removeDataChangedCallback(e, t)
                            ? r.delete(e)
                            : console.error("Can't remove callback by id:", e);
                        }
                        engine.whenReady.then(() => {
                          engine.on("viewEnv.onDataChanged", (e, t, u) => {
                            u.forEach((t) => {
                              const u = r.get(t);
                              void 0 !== u && u(e);
                            });
                          });
                        });
                        const a = (e) => {
                          const r = u(t),
                            o = n.split(".").reduce((e, t) => e[t], r);
                          return "string" != typeof e || 0 === e.length
                            ? o
                            : e.split(".").reduce((e, t) => {
                                const u = e[t];
                                return "function" == typeof u ? u.bind(e) : u;
                              }, o);
                        };
                        return {
                          subscribe: (u, o) => {
                            const i = "string" == typeof o ? `${n}.${o}` : n,
                              s = l.O.view.addModelObserver(i, t, !0);
                            return (r.set(s, u), e && u(a(o)), s);
                          },
                          readByPath: a,
                          createCallback: (e, t) => {
                            const u = a(t);
                            return (...t) => {
                              u(e(...t));
                            };
                          },
                          createCallbackNoArgs: (e) => {
                            const t = a(e);
                            return () => {
                              t();
                            };
                          },
                          dispose: function () {
                            for (var e, u = on(r.keys()); !(e = u()).done;) o(e.value, t);
                          },
                          unsubscribe: o,
                        };
                      })(n),
                      i =
                        "real" === u
                          ? a
                          : Object.assign({}, a, {
                              readByPath:
                                null != (o = null == r ? void 0 : r.getter) ? o : () => {},
                            }),
                      s = (e) =>
                        "mocks" === u ? (null == r ? void 0 : r.getter(e)) : i.readByPath(e),
                      d = (e) => c.current.push(e),
                      m = e({
                        mode: u,
                        readByPath: s,
                        externalModel: i,
                        observableModel: {
                          array: (e, t) => {
                            const n = null != t ? t : s(e),
                              r = rn.LO.box(n, { equals: nn });
                            return (
                              "real" === u &&
                                i.subscribe(
                                  (0, rn.aD)((e) => r.set(e)),
                                  e,
                                ),
                              r
                            );
                          },
                          object: (e, t) => {
                            const n = null != t ? t : s(e),
                              r = rn.LO.box(n, { equals: nn });
                            return (
                              "real" === u &&
                                i.subscribe(
                                  (0, rn.aD)((e) => r.set(e)),
                                  e,
                                ),
                              r
                            );
                          },
                          primitives: (e, t) => {
                            const n = s(t);
                            if (Array.isArray(e)) {
                              const r = e.reduce((e, t) => ((e[t] = rn.LO.box(n[t], {})), e), {});
                              return (
                                "real" === u &&
                                  i.subscribe(
                                    (0, rn.aD)((t) => {
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
                                a = o.reduce((e, [t, u]) => ((e[u] = rn.LO.box(n[t], {})), e), {});
                              return (
                                "real" === u &&
                                  i.subscribe(
                                    (0, rn.aD)((e) => {
                                      o.forEach(([t, u]) => {
                                        a[u].set(e[t]);
                                      });
                                    }),
                                    t,
                                  ),
                                a
                              );
                            }
                          },
                        },
                        cleanup: d,
                      }),
                      E = { mode: u, model: m, externalModel: i, cleanup: d };
                    return {
                      model: m,
                      controls: "mocks" === u && r ? r.controls(E) : t(E),
                      externalModel: i,
                      mode: u,
                    };
                  },
                  m = (0, o.useRef)(!1),
                  E = (0, o.useState)(n),
                  _ = E[0],
                  h = E[1],
                  A = (0, o.useState)(() => d(n, r, s)),
                  p = A[0],
                  g = A[1];
                return (
                  (0, o.useEffect)(() => {
                    m.current ? g(d(_, r, s)) : (m.current = !0);
                  }, [s, _, r]),
                  (0, o.useEffect)(() => {
                    h(n);
                  }, [n]),
                  (0, o.useEffect)(
                    () => () => {
                      (p.externalModel.dispose(), c.current.forEach((e) => e()));
                    },
                    [p],
                  ),
                  a().createElement(u.Provider, { value: p }, i)
                );
              },
              () => (0, o.useContext)(u),
            ];
          })(
            ({ observableModel: e }) => {
              const t = {
                  root: e.object(),
                  items: e.array("items"),
                  tabs: e.array("tabs"),
                  confirmationTabs: e.array("confirmationTabs"),
                  selectedItemsCounter: e.array("selectedItemsCounter"),
                  activeTabId: e.array("activeTabId"),
                },
                u = (0, En.Om)(() => mn(t.items.get()), { equals: nn }),
                n = (0, En.Om)(() => cn(u(), (e) => e.selectedCount > 0), { equals: nn }),
                r = (0, En.Om)(
                  () => {
                    var e;
                    return null == (e = n()) ? void 0 : e.intCD;
                  },
                  { equals: nn },
                ),
                o = (0, En.Om)(() => mn(t.tabs.get()), { equals: nn }),
                a = (0, En.Om)(() => cn(o(), (e) => e.isSelected), { equals: nn }),
                i = (0, En.Om)(() => mn(t.confirmationTabs.get()), { equals: nn });
              return Object.assign({}, t, {
                computes: {
                  getItems: u,
                  getTabs: o,
                  getSelectedItem: n,
                  getSelectedItemId: r,
                  getSelectedTab: a,
                  getConfirmationTabs: i,
                },
              });
            },
            ({ externalModel: e }) => ({
              onClose: e.createCallbackNoArgs("onClose"),
              onShowInfo: e.createCallbackNoArgs("onShowInfo"),
              onExchange: e.createCallback(() => ({}), "onExchange"),
              onSelectItem: e.createCallback((e) => ({ itemId: e }), "onSelectItem"),
              onUnselectItem: e.createCallbackNoArgs("onUnselectItem"),
              selectTab: e.createCallback((e) => ({ tabId: e }), "onTabChange"),
              hoverTab: e.createCallback((e) => ({ tabId: e }), "onHoverTab"),
              changeFilter: e.createCallback((e, t) => ({ key: e, value: t }), "changeFilter"),
              clearFilter: e.createCallbackNoArgs("clearFilter"),
              selectAll: e.createCallbackNoArgs("onSelectAll"),
              onAdd: e.createCallback((e, t) => ({ intCD: e, vehicleCD: t }), "onAdd"),
              onReduce: e.createCallback((e, t) => ({ intCD: e, vehicleCD: t }), "onReduce"),
              showExchangeConfirmation: e.createCallbackNoArgs("onShowExchangeConfirmation"),
              closeExchangeConfirmation: e.createCallbackNoArgs("onCloseExchangeConfirmation"),
              captchaChange: e.createCallback((e) => ({ value: e }), "onCaptchaChange"),
              confirmExchange: e.createCallbackNoArgs("onConfirmExchange"),
              loadCards: e.createCallback(
                (e, t) => ({ startIndex: e, endIndex: t }),
                "onLoadCards",
              ),
            }),
          ),
          hn = _n[0],
          An = _n[1],
          pn = {
            base: "App_base_64",
            header: "App_header_d2",
            filters: "App_filters_80",
            paintsIcon: "App_paintsIcon_c4",
            paintsHolder: "App_paintsHolder_b0",
            paintsBalance: "App_paintsBalance_b7",
            paintsTotal: "App_paintsTotal_99",
            currency: "App_currency_41",
            currencyHolder: "App_currencyHolder_cf",
            limitsHolder: "App_limitsHolder_0d",
            title: "App_title_e1",
            subTitle: "App_subTitle_ab",
            aboutButton: "App_aboutButton_99",
            filterHeader: "App_filterHeader_f5",
            filterCounter: "App_filterCounter_2b",
            filterNumbers: "App_filterNumbers_78",
            filterNumbersLabel: "App_filterNumbersLabel_0f",
            closeButton: "App_closeButton_88",
            carouselWrapper: "App_carouselWrapper_0e",
            scrollArea: "App_scrollArea_80",
            itemsHolder: "App_itemsHolder_55",
            scrollContent: "App_scrollContent_6a",
            scrollContent__withoutScroll: "App_scrollContent__withoutScroll_f6",
            scrollContent__transition: "App_scrollContent__transition_c7",
            emptyState: "App_emptyState_f6",
            scrollbarWrapper: "App_scrollbarWrapper_96",
            priceWrapper: "App_priceWrapper_d6",
            price: "App_price_98",
            exchangeText: "App_exchangeText_e6",
            exchangeEnableText: "App_exchangeEnableText_b5",
            limitText: "App_limitText_66",
            exchangeButton: "App_exchangeButton_73",
            triggerButton: "App_triggerButton_90",
            categories: "App_categories_dd",
            categoriesBackground: "App_categoriesBackground_ae",
            category: "App_category_be",
            divider: "App_divider_ec",
            reward: "App_reward_ba",
          };
        function gn() {
          return (
            (gn =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            gn.apply(this, arguments)
          );
        }
        const bn = ({ children: e, tooltipArgs: t, className: u }) => {
            if (!t) return e;
            const n = a().createElement("div", { className: u }, e);
            if (t.header || t.body) return a().createElement(Gt, t, n);
            const r = t.contentId,
              o = t.args,
              i = null == o ? void 0 : o.contentId;
            return r || i
              ? a().createElement(Nt, gn({}, t, { contentId: r || i }), n)
              : a().createElement(ou, t, n);
          },
          Cn = ["children", "tooltipType", "wrap"],
          Fn = ["contentId"];
        function fn() {
          return (
            (fn =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            fn.apply(this, arguments)
          );
        }
        function Dn(e, t) {
          if (null == e) return {};
          var u,
            n,
            r = {},
            o = Object.keys(e);
          for (n = 0; n < o.length; n++) ((u = o[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
          return r;
        }
        let vn;
        !(function (e) {
          ((e.Base = "base"), (e.Backport = "backport"), (e.Simple = "simple"));
        })(vn || (vn = {}));
        const Bn = (e) => {
            let t = e.children,
              u = e.tooltipType,
              n = e.wrap,
              r = void 0 !== n && n,
              o = Dn(e, Cn);
            if (!o) return t;
            const i =
                r && (o.isEnabled || void 0 === o.isEnabled)
                  ? a().createElement("div", null, t)
                  : t,
              l = o.contentId,
              s = Dn(o, Fn);
            switch (u) {
              case vn.Base:
                return (
                  !l && console.error("`contentId` field is required for a base Tooltip"),
                  l ? a().createElement(Nt, fn({}, s, { contentId: l }), i) : i
                );
              case vn.Simple:
                return a().createElement(Gt, s, i);
              case vn.Backport:
                return a().createElement(ou, s, i);
              default:
                return a().createElement(bn, { tooltipArgs: o }, i);
            }
          },
          wn = "default",
          Sn = "search",
          yn = "email",
          xn = "password",
          Tn = "normal",
          Ln = "disabled",
          Mn = "alert",
          Rn = "error",
          kn = "medium",
          Nn = "large",
          Pn = {
            [wn]: "",
            [yn]: R.strings.common.input.placeholder.email(),
            [Sn]: R.strings.common.input.placeholder.search(),
            [xn]: R.strings.common.input.placeholder.password(),
          },
          On = { [wn]: "text", [yn]: "text", [Sn]: "text", [xn]: "password" },
          Hn = { [wn]: "", [yn]: "Invalid email", [Sn]: "", [xn]: "" },
          In = R.images.gui.maps.icons.components.input;
        function Wn(e, t) {
          return (
            t !== yn ||
            (function (e) {
              const t = e.match(
                /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/,
              );
              return Boolean(t);
            })(e)
          );
        }
        const Xn = {
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
          Yn = a().memo(
            ({
              componentId: e,
              value: t = "",
              type: u = wn,
              size: n = kn,
              variant: r = Tn,
              placeholder: i = "",
              highlighted: l,
              withClear: s,
              selectOnFocus: c = !0,
              maxLength: d,
              iconSource: m,
              classMix: E,
              onMouseEnter: _,
              onMouseLeave: h,
              onMouseDown: A,
              onMouseUp: p,
              onClick: g,
              onChange: b,
              onClear: C,
              onFocus: F,
              onBlur: D,
            }) => {
              const v = (0, o.useState)(!1),
                B = v[0],
                w = v[1],
                S = (0, o.useRef)(null),
                y = (0, o.useRef)({ mouseOver: !1, mouseDown: !1 }),
                x = r !== Ln,
                T = (0, o.useCallback)(
                  (e) => {
                    x && (w(!0), F && F(e));
                  },
                  [x, F],
                ),
                L = (0, o.useCallback)(
                  (e) => {
                    x && !y.current.mouseOver && (w(!1), D && D(e));
                  },
                  [x, D],
                );
              (0, o.useEffect)(() => {
                x && B && c && S.current && S.current.select();
              }, [c, B, x]);
              const M = (0, o.useCallback)(
                  (e) => {
                    x && b && b(e.target.value);
                  },
                  [x, b],
                ),
                R = (0, o.useCallback)(
                  (e) => {
                    x && ((y.current.mouseOver = !0), _ && _(e));
                  },
                  [x, _],
                ),
                k = (0, o.useCallback)(
                  (e) => {
                    x &&
                      S.current &&
                      (y.current.mouseDown && S.current.focus(),
                      (y.current.mouseOver = !1),
                      h && h(e));
                  },
                  [x, h],
                ),
                N = (0, o.useCallback)(
                  (e) => {
                    x && ((y.current.mouseDown = !0), A && A(e));
                  },
                  [x, A],
                ),
                P = (0, o.useCallback)(
                  (e) => {
                    x && ((y.current.mouseDown = !1), p && p(e));
                  },
                  [x, p],
                ),
                O = (0, o.useCallback)(
                  (e) => {
                    if (x && S.current) {
                      ((!B || (B && e.target !== S.current)) && S.current.focus(), g && g(e));
                    }
                  },
                  [B, x, g],
                ),
                H = i || Pn[u],
                I = Boolean(m),
                W = f()(
                  Xn.base,
                  Xn[`base__${n}`],
                  l && Xn[`base__${r}`],
                  B && Xn.base__focused,
                  I && Xn.base__withIcon,
                  E,
                ),
                Y = (0, o.useMemo)(() => (m ? { backgroundImage: `url(${m})` } : null), [m]),
                z = f()(Xn.input, Xn[`input__${u}`]),
                U = f()(Xn.icon, Xn[`icon__${u}`]),
                G = f()(Xn.placeholder, Xn[`placeholder__${u}`]);
              return a().createElement(
                "div",
                {
                  id: e,
                  className: W,
                  onMouseEnter: R,
                  onMouseDown: N,
                  onMouseUp: P,
                  onMouseLeave: k,
                  onClick: O,
                },
                !x && a().createElement("div", { className: Xn.disabled }),
                Y && a().createElement("div", { style: Y, className: U }),
                a().createElement("input", {
                  ref: S,
                  className: z,
                  type: On[u],
                  value: t,
                  onChange: M,
                  disabled: !x,
                  onFocus: T,
                  onBlur: L,
                  maxLength: d,
                }),
                H && !t && !B && a().createElement("div", { className: G }, H),
                s &&
                  a().createElement("div", {
                    className: Xn.clear,
                    onClick: (e) => {
                      (X.playClick(), C && C(e));
                    },
                    onMouseEnter: X.playHighlight,
                  }),
              );
            },
          ),
          zn = {
            base: "HelperMessage_base_1e",
            base__shown: "HelperMessage_base__shown_ab",
            icon: "HelperMessage_icon_10",
            message: "HelperMessage_message_f4",
            message__alert: "HelperMessage_message__alert_b5",
            message__error: "HelperMessage_message__error_45",
            message__done: "HelperMessage_message__done_2b",
          },
          Un = ({ variant: e, show: t = !0, helperText: u, helperIcon: n, classMix: r }) => {
            const i = (0, o.useMemo)(() => {
                const t =
                  n ||
                  (function (e) {
                    return e === Mn ? R.images.gui.maps.icons.library.alertIcon() : "";
                  })(e);
                return t && { backgroundImage: `url(${t})` };
              }, [n, e]),
              l = f()(zn.base, t && zn.base__shown),
              s = f()(zn.message, zn[`message__${e}`], r);
            return a().createElement(
              "div",
              { className: l },
              i && a().createElement("div", { className: zn.icon, style: i }),
              a().createElement("div", { className: s }, u),
            );
          },
          Gn = {
            base: "Input_base_cd",
            base__small: "Input_base__small_c7",
            base__medium: "Input_base__medium_1f",
            base__large: "Input_base__large_11",
            helper: "Input_helper_ea",
          },
          jn = [
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
        function Vn() {
          return (
            (Vn =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            Vn.apply(this, arguments)
          );
        }
        const $n = {
            debounceTime: 200,
            performChangeValidation: !0,
            selectOnFocus: !0,
            withTypeIcon: !0,
            disableHighlightOnFocus: !0,
          },
          qn = (e) => {
            let t = e.componentId,
              u = e.type,
              n = void 0 === u ? wn : u,
              r = e.variant,
              i = void 0 === r ? Tn : r,
              l = e.size,
              s = void 0 === l ? kn : l,
              c = e.value,
              d = e.tooltipArgs,
              m = e.helperText,
              E = void 0 === m ? "" : m,
              _ = e.isValidated,
              h = void 0 === _ || _,
              A = e.showHelper,
              p = void 0 === A || A,
              g = e.error,
              b = e.options,
              C = e.onFocus,
              F = e.onMouseEnter,
              D = e.onMouseLeave,
              v = e.onMouseUp,
              B = e.onMouseDown,
              w = e.onChange,
              S = e.classMix,
              y = e.controlClassMix,
              x = e.helperClassMix,
              T = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  r = {},
                  o = Object.keys(e);
                for (n = 0; n < o.length; n++) ((u = o[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
                return r;
              })(e, jn);
            const L = (0, o.useState)(c),
              M = L[0],
              R = L[1],
              k = (0, o.useState)(h),
              N = k[0],
              P = k[1],
              O = (0, o.useMemo)(() => Object.assign({}, $n, b), [b]),
              H = (0, o.useRef)({ debounceTimeout: 0, isChangeHandled: !0, value: c, type: n }),
              I = (0, o.useCallback)((e) => {
                e !== H.current.value &&
                  ((H.current.value = e), (H.current.isChangeHandled = !1), R(e));
              }, []),
              W = (0, o.useCallback)(
                (e) => {
                  let t = !0;
                  (O.performChangeValidation &&
                    (t = O.changesValidator ? O.changesValidator(e) : Wn(e, H.current.type)),
                    w && w(e, t));
                },
                [w, O],
              ),
              X = (0, o.useCallback)(() => {
                H.current.debounceTimeout &&
                  (window.clearTimeout(H.current.debounceTimeout), (H.current.debounceTimeout = 0));
              }, []),
              Y = (0, o.useCallback)(() => I(""), [I]);
            (0, o.useEffect)(() => () => X(), [X]);
            const z = (0, o.useCallback)(
              (e) => {
                (X(),
                  O.debounceTime
                    ? (H.current.debounceTimeout = window.setTimeout(() => {
                        W(e);
                      }, O.debounceTime))
                    : W(e));
              },
              [W, X, O.debounceTime],
            );
            ((0, o.useEffect)(() => {
              H.current.isChangeHandled ||
                H.current.value !== M ||
                (z(H.current.value), (H.current.isChangeHandled = !0));
            }, [M, z]),
              (0, o.useEffect)(() => {
                (H.current.isChangeHandled &&
                  c !== H.current.value &&
                  ((H.current.value = c), R(c)),
                  (H.current.type = n));
              }, [c, n]),
              (0, o.useEffect)(() => {
                P(h);
              }, [h, i]));
            const U = (0, o.useCallback)((e) => F && F(e), [F]),
              G = (0, o.useCallback)(
                (e) => {
                  (O.disableHighlightOnFocus && N && P(!1), C && C(e));
                },
                [N, C, O.disableHighlightOnFocus],
              ),
              j = (0, o.useCallback)((e) => v && v(e), [v]),
              V = (0, o.useCallback)((e) => B && B(e), [B]),
              $ = (0, o.useCallback)((e) => D && D(e), [D]),
              q = (0, o.useMemo)(
                () =>
                  O.withTypeIcon
                    ? (function (e, t) {
                        return e === Sn ? In.$dyn(`search_${t}`) : "";
                      })(n, s)
                    : "",
                [n, s, O.withTypeIcon],
              ),
              K = E || Hn[n],
              Q = Boolean(M),
              Z = g ? Rn : i,
              J = Boolean(g) || N,
              ee = (0, o.useMemo)(
                () => ("boolean" == typeof O.withClear ? Q && O.withClear : Q && n === Sn),
                [n, Q, O],
              ),
              te = f()(Gn.base, Gn[`base__${s}`], Gn[`base__${i}`], S);
            return a().createElement(
              "div",
              {
                id: t,
                className: te,
                onMouseEnter: U,
                onMouseDown: V,
                onMouseUp: j,
                onMouseLeave: $,
              },
              a().createElement(
                Bn,
                Vn({ wrap: !0 }, d),
                a().createElement(
                  Yn,
                  Vn(
                    {
                      componentId: t ? `${t}-inputControl` : void 0,
                      iconSource: q,
                      size: s,
                      type: n,
                      variant: Z,
                      value: M,
                      withClear: ee,
                      highlighted: J,
                      selectOnFocus: O.selectOnFocus,
                      maxLength: O.maxLength,
                      classMix: y,
                      onFocus: G,
                      onChange: I,
                      onClear: Y,
                    },
                    T,
                  ),
                ),
              ),
              K &&
                a().createElement(
                  "div",
                  { className: Gn.helper },
                  a().createElement(Un, {
                    variant: Z,
                    show: p && (O.isPermanentHelper || J),
                    helperText: g || K,
                    helperIcon: O.helperIconSource,
                    classMix: x,
                  }),
                ),
            );
          };
        function Kn(e, t, u) {
          const n = (0, o.useMemo)(
            () =>
              (function (e, t, u) {
                return void 0 === u ? ue(e, t, !1) : ue(e, u, !1 !== t);
              })(u, e),
            t,
          );
          return ((0, o.useEffect)(() => n.cancel, [n]), n);
        }
        const Qn = "ExchangeConfirmationScreen_overlay_d4",
          Zn = "ExchangeConfirmationScreen_background_3c",
          Jn = "ExchangeConfirmationScreen_closeButton_80",
          er = "ExchangeConfirmationScreen_content_18",
          tr = "ExchangeConfirmationScreen_title_17",
          ur = "ExchangeConfirmationScreen_tabsWrapper_a8",
          nr = "ExchangeConfirmationScreen_tabs_c4",
          rr = "ExchangeConfirmationScreen_tab_79",
          or = "ExchangeConfirmationScreen_tabImage_e0",
          ar = "ExchangeConfirmationScreen_tabTitle_82",
          ir = "ExchangeConfirmationScreen_tabCount_40",
          lr = "ExchangeConfirmationScreen_captcha_f2",
          sr = "ExchangeConfirmationScreen_warning_12",
          cr = "ExchangeConfirmationScreen_warningHighlight_ae",
          dr = "ExchangeConfirmationScreen_captchaPrompt_b3",
          mr = "ExchangeConfirmationScreen_input_33",
          Er = "ExchangeConfirmationScreen_inputControl_6c",
          _r = "ExchangeConfirmationScreen_inputHelper_46",
          hr = "ExchangeConfirmationScreen_footer_c8",
          Ar = "ExchangeConfirmationScreen_reward_86",
          pr = "ExchangeConfirmationScreen_rewardLabel_10",
          gr = "ExchangeConfirmationScreen_currency_c9",
          br = "ExchangeConfirmationScreen_currencyIcon_b1",
          Cr = "ExchangeConfirmationScreen_buttons_b0",
          Fr = "ExchangeConfirmationScreen_button_e8",
          fr = "ExchangeConfirmationScreen_button__close_a2",
          Dr = "ExchangeConfirmationScreen_exchangeItemsCount_8f",
          vr = "ExchangeConfirmationScreen_limitsHolder_56",
          Br = "ExchangeConfirmationScreen_limitText_63",
          wr = "ExchangeConfirmationScreen_paintsTotal_bb",
          Sr = R.strings.event.customizationResource,
          yr = "customizationResourceExchangeCaptcha",
          xr = (0, Xt.Pi)(() => {
            const e = An(),
              t = e.controls,
              u = e.model,
              n = u.computes.getConfirmationTabs(),
              r = (0, o.useState)(""),
              i = r[0],
              l = r[1],
              s = (0, o.useState)(0),
              c = s[0],
              d = s[1],
              m = (0, o.useRef)(!1),
              E = u.root.get(),
              _ = E.exchangeItemsCount,
              h = E.selectedCount,
              A = E.limit,
              p = E.captchaState,
              g = E.exchangeReward,
              b = y().mediaSize,
              C = 1 === p,
              F = 2 === p,
              D = Sr.exchangeConfirmation.warning().split(/<\/?b>/),
              v = D[0],
              w = void 0 === v ? "" : v,
              S = D[1],
              x = void 0 === S ? "" : S,
              T = D[2],
              L = void 0 === T ? "" : T,
              M = b <= B.Small ? U.small : U.medium;
            (It({ callback: t.closeExchangeConfirmation }),
              (0, o.useEffect)(() => {
                (l(""), d((e) => e + 1));
              }, [_]),
              (0, o.useEffect)(() => {
                var e, t;
                m.current &&
                  ((m.current = !1),
                  null == (e = document.getElementById(`${yr}-inputControl`)) ||
                    null == (t = e.querySelector("input")) ||
                    t.focus());
              }, [c]));
            const k = Kn((e) => t.captchaChange(e), [t], 200),
              N = (0, o.useCallback)(
                (e) => {
                  const t = e.replace(/\D/g, "");
                  (l(t), t !== e && ((m.current = !0), d((e) => e + 1)), k(t));
                },
                [k],
              ),
              P = (0, o.useMemo)(
                () =>
                  n.map((e) => {
                    return a().createElement(
                      Nt,
                      {
                        contentId:
                          R.views.lobby.customization_resource.tooltips.CategoryTooltipView(
                            "resId",
                          ),
                        args: { tabId: e.tabId },
                        key: e.tabId,
                      },
                      a().createElement(
                        "div",
                        { className: rr },
                        a().createElement(St, {
                          className: ar,
                          text: String(Sr.tabs.items.$dyn(e.itemType)),
                        }),
                        a().createElement("div", {
                          className: or,
                          style: {
                            backgroundImage: `url(${((t = e.itemType), R.images.gui.maps.icons.quests.bonuses.big.$dyn(t))})`,
                          },
                        }),
                        a().createElement(St, {
                          className: ir,
                          text: String(e.selectedCount || 0),
                        }),
                      ),
                    );
                    var t;
                  }),
                [n],
              );
            return a().createElement(
              "div",
              { className: Qn },
              a().createElement("div", { className: Zn }),
              a().createElement(
                "div",
                { className: Jn },
                a().createElement(Lt, {
                  side: "right",
                  type: "close",
                  caption: Sr.mainView.closeButton(),
                  onClick: t.closeExchangeConfirmation,
                }),
              ),
              a().createElement(
                "div",
                { className: er },
                a().createElement(St, { className: tr, text: Sr.exchangeConfirmation.title() }),
                a().createElement(
                  "div",
                  { className: ur },
                  a().createElement("div", { className: nr }, P),
                ),
                a().createElement(
                  "div",
                  { className: lr },
                  a().createElement(
                    "div",
                    { className: sr },
                    a().createElement(St, { text: w }),
                    a().createElement(St, { className: cr, text: x }),
                    a().createElement(St, { text: L }),
                  ),
                  a().createElement(St, {
                    className: dr,
                    text: Sr.exchangeConfirmation.captcha.prompt(),
                    format: {
                      binding: { count: a().createElement(St, { text: String(_), className: Dr }) },
                    },
                  }),
                  a().createElement(qn, {
                    key: c,
                    componentId: yr,
                    classMix: mr,
                    controlClassMix: Er,
                    helperClassMix: _r,
                    size: Nn,
                    value: i,
                    variant: C ? "error" : "normal",
                    helperText: C ? Sr.exchangeConfirmation.captcha.error() : void 0,
                    showHelper: C,
                    options: {
                      debounceTime: 0,
                      performChangeValidation: !1,
                      selectOnFocus: !0,
                      withTypeIcon: !1,
                    },
                    onChange: N,
                  }),
                ),
                a().createElement(
                  "div",
                  { className: hr },
                  a().createElement(
                    "div",
                    { className: Ar },
                    a().createElement(St, {
                      text: Sr.mainView.exchangeSelectedText(),
                      className: pr,
                    }),
                    a().createElement(St, {
                      text: Sr.mainView.counter(),
                      className: vr,
                      format: {
                        binding: {
                          selectedCount: a().createElement(
                            "div",
                            { className: wr },
                            a().createElement($, { value: h }),
                          ),
                          availableCount: a().createElement($, { value: A }),
                        },
                      },
                    }),
                    a().createElement(St, {
                      className: pr,
                      text: Sr.exchangeConfirmation.reward(),
                    }),
                    a().createElement(
                      Nt,
                      {
                        contentId:
                          R.views.lobby.customization_resource.tooltips.CustomizationResourceCurrencyTooltipView(
                            "resId",
                          ),
                      },
                      a().createElement(
                        "div",
                        { className: gr },
                        a().createElement($, { value: g }),
                        a().createElement("div", { className: br }),
                      ),
                    ),
                  ),
                  a().createElement(
                    "div",
                    { className: Cr },
                    a().createElement(
                      j,
                      {
                        mixClass: Fr,
                        type: z.primary,
                        size: M,
                        onClick: t.confirmExchange,
                        disabled: !F,
                      },
                      a().createElement(St, { text: Sr.exchangeConfirmation.confirm() }),
                    ),
                    a().createElement(
                      j,
                      {
                        mixClass: f()(Fr, fr),
                        type: z.secondary,
                        size: M,
                        onClick: t.closeExchangeConfirmation,
                      },
                      a().createElement(St, { text: Sr.exchangeConfirmation.cancel() }),
                    ),
                  ),
                ),
              ),
              a().createElement(St, {
                text: Sr.mainView.limitText(),
                className: Br,
                format: { binding: { limit: a().createElement($, { value: A }) } },
              }),
            );
          });
        let Tr;
        !(function (e) {
          ((e[(e.LEFT = 0)] = "LEFT"),
            (e[(e.WHEEL = 1)] = "WHEEL"),
            (e[(e.RIGHT = 2)] = "RIGHT"),
            (e[(e.FOURTH = 3)] = "FOURTH"),
            (e[(e.FIFTH = 4)] = "FIFTH"));
        })(Tr || (Tr = {}));
        const Lr = {
          base: "Checkbox_base_36",
          base__disabled: "Checkbox_base__disabled_08",
          base__center: "Checkbox_base__center_52",
          base__bottom: "Checkbox_base__bottom_28",
          input: "Checkbox_input_37",
          base__mouseDown: "Checkbox_base__mouseDown_45",
          base__small: "Checkbox_base__small_18",
          base__medium: "Checkbox_base__medium_12",
          base__large: "Checkbox_base__large_f7",
          base__extraLarge: "Checkbox_base__extraLarge_c9",
          alertOverlay: "Checkbox_alertOverlay_52",
          base__alert: "Checkbox_base__alert_b7",
          blink: "Checkbox_blink_5e",
          base__checked: "Checkbox_base__checked_a2",
          inputHoverOverlay: "Checkbox_inputHoverOverlay_36",
          highlight: "Checkbox_highlight_b8",
          base__main: "Checkbox_base__main_3a",
          base__primary: "Checkbox_base__primary_ab",
          checkmark: "Checkbox_checkmark_60",
          fadeIn: "Checkbox_fadeIn_1a",
          label: "Checkbox_label_bc",
          labelContent: "Checkbox_labelContent_64",
        };
        let Mr, Rr, kr;
        (!(function (e) {
          ((e.small = "small"),
            (e.medium = "medium"),
            (e.large = "large"),
            (e.extraLarge = "extraLarge"));
        })(Mr || (Mr = {})),
          (function (e) {
            ((e.primary = "primary"), (e.main = "main"));
          })(Rr || (Rr = {})),
          (function (e) {
            ((e.Center = "center"), (e.Bottom = "bottom"));
          })(kr || (kr = {})));
        const Nr = [
          "id",
          "isChecked",
          "isDisabled",
          "isAlert",
          "size",
          "type",
          "soundHover",
          "soundClick",
          "onMouseEnter",
          "onMouseLeave",
          "onMouseUp",
          "onMouseDown",
          "onClick",
          "onChange",
          "onFocus",
          "onBlur",
          "text",
          "contentStyles",
          "children",
          "alignment",
        ];
        function Pr() {
          return (
            (Pr =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            Pr.apply(this, arguments)
          );
        }
        const Or = (e) => {
            let t = e.id,
              u = e.isChecked,
              n = void 0 !== u && u,
              r = e.isDisabled,
              i = void 0 !== r && r,
              l = e.isAlert,
              s = void 0 !== l && l,
              c = e.size,
              d = void 0 === c ? Mr.medium : c,
              m = e.type,
              E = void 0 === m ? Rr.primary : m,
              _ = e.soundHover,
              h = void 0 === _ ? "highlight" : _,
              A = e.soundClick,
              p = void 0 === A ? "play" : A,
              g = e.onMouseEnter,
              b = e.onMouseLeave,
              C = e.onMouseUp,
              F = e.onMouseDown,
              D = e.onClick,
              v = e.onChange,
              B = e.onFocus,
              w = e.onBlur,
              S = e.text,
              y = e.contentStyles,
              x = e.children,
              T = e.alignment,
              L = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  r = {},
                  o = Object.keys(e);
                for (n = 0; n < o.length; n++) ((u = o[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
                return r;
              })(e, Nr);
            const M = (0, o.useState)(!1),
              R = M[0],
              k = M[1],
              N = (0, o.useState)(!1),
              P = (N[0], N[1]),
              O = (0, o.useCallback)(
                (e) => {
                  i || (v && v(), D && D(e));
                },
                [i, v, D],
              ),
              H = (0, o.useCallback)(
                (e) => {
                  const t = e.button === Tr.LEFT;
                  i || (t && k(!0), t && F && F(e), p && W(p));
                },
                [i, F, p],
              ),
              I = (0, o.useCallback)(
                (e) => {
                  i || (k(!1), C && C(e));
                },
                [i, C],
              ),
              X = (0, o.useCallback)(
                (e) => {
                  i || (g && g(e), h && W(h));
                },
                [i, g, h],
              ),
              Y = (0, o.useCallback)(
                (e) => {
                  i || (k(!1), b && b(e));
                },
                [i, b],
              ),
              z = (0, o.useCallback)(
                (e) => {
                  i || (P(!0), B && B(e));
                },
                [i, B],
              ),
              U = (0, o.useCallback)(
                (e) => {
                  i || (P(!1), w && w(e));
                },
                [i, w],
              ),
              G = a().createElement(
                "div",
                { className: Lr.label },
                a().createElement(
                  "div",
                  { className: f()(Lr.labelContent, "s-labelContent"), style: y },
                  S || x,
                ),
              );
            return a().createElement(
              "div",
              Pr(
                {
                  id: t,
                  className: f()(Lr.base, Lr[`base__${d}`], Lr[`base__${E}`], {
                    [Lr.base__checked]: n,
                    [Lr.base__disabled]: i,
                    [Lr.base__mouseDown]: R,
                    [Lr.base__alert]: s,
                    [Lr.base__center]: T === kr.Center,
                    [Lr.base__bottom]: T === kr.Bottom,
                  }),
                  onClick: O,
                  onMouseEnter: X,
                  onMouseLeave: Y,
                  onMouseDown: H,
                  onMouseUp: I,
                  onFocus: z,
                  onBlur: U,
                },
                L,
              ),
              a().createElement(
                "div",
                { className: Lr.input },
                a().createElement("div", { className: Lr.alertOverlay }),
                a().createElement("div", { className: Lr.inputHoverOverlay }),
                a().createElement("div", { className: Lr.highlight }),
              ),
              a().createElement("div", { className: Lr.checkmark }),
              ((S || x) && G) || null,
            );
          },
          Hr = (e) => {
            (0, o.useEffect)(e, []);
          },
          Ir = {
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
        var Wr;
        !(function (e) {
          ((e[(e.Left = 0)] = "Left"),
            (e[(e.Right = 1)] = "Right"),
            (e[(e.Top = 2)] = "Top"),
            (e[(e.Bottom = 3)] = "Bottom"));
        })(Wr || (Wr = {}));
        const Xr = ["__left", "__right", "__top", "__bottom"],
          Yr =
            ((0, o.forwardRef)(
              (
                { children: e, disableAutoSizeUpdate: t, onOutsideClick: u, customStyles: n = {} },
                r,
              ) => {
                const i = (0, o.useRef)(null),
                  s = (0, o.useRef)(null),
                  c = (0, o.useRef)(null),
                  d = (0, o.useState)(window.decorator && window.decorator.directionType),
                  m = d[0],
                  E = d[1],
                  _ = (0, o.useCallback)(() => {
                    (X.playClick(), l.O.view.sendEvent.close());
                  }, []),
                  h = (0, o.useCallback)(() => {
                    X.playHighlight();
                  }, []),
                  A = f()(Ir.arrow, Ir[`arrow${Xr[m]}`]);
                Hr(
                  () => (
                    l.O.client.events.mouse.enableOutside(),
                    l.O.client.events.mouse.down(([, e]) => {
                      "outside" === e && (u ? u() : l.O.view.sendEvent.close("popover"));
                    })
                  ),
                );
                const p = (0, o.useCallback)(
                    (e) => {
                      let t = e.target;
                      do {
                        if (t === i.current || t === c.current) return;
                        t = t.parentNode;
                      } while (t);
                      const n = window.decorator;
                      if (void 0 !== window.decorator) {
                        const e = l.O.client.getMouseGlobalPosition(),
                          t = ![n.boundX, n.boundY, n.boundWidth, n.boundHeight].includes(void 0),
                          u =
                            e.x < n.boundX ||
                            e.x > n.boundX + n.boundWidth ||
                            e.y > n.boundY + n.boundHeight ||
                            e.y < n.boundY;
                        if (t && !u) return;
                      }
                      u ? u() : l.O.view.sendEvent.close("popover");
                    },
                    [i, c, u],
                  ),
                  g = (0, o.useCallback)(
                    () => (
                      l.O.view.freezeTextureBeforeResize(),
                      q(() => {
                        if (s.current) {
                          const e = s.current.scrollWidth,
                            t = s.current.scrollHeight;
                          (l.O.view.resize(e, t), E(window.decorator.directionType));
                        }
                      })
                    ),
                    [],
                  );
                return (
                  (0, o.useImperativeHandle)(r, () => ({ updateSize: g })),
                  Hr(() => {
                    l.O.view.setInputPaddingsRem(58);
                  }),
                  (0, o.useEffect)(() => {
                    document.addEventListener("mousedown", p, { capture: !0 });
                    const e = ((e) => {
                      let t = !1;
                      return {
                        promise: new Promise((u, n) => {
                          e.then((e) => !t && u(e)).catch((e) => !t && n(e));
                        }),
                        cancel() {
                          t = !0;
                        },
                      };
                    })((0, V.Eu)());
                    return (
                      !t && e.promise.then(() => g()),
                      () => {
                        (e.cancel(), document.removeEventListener("mousedown", p));
                      }
                    );
                  }, [g, p, t]),
                  a().createElement(
                    "div",
                    { className: Ir.base, ref: s },
                    a().createElement(
                      "div",
                      { className: Ir.decorator },
                      a().createElement(
                        "div",
                        { className: Ir.content, ref: i },
                        e,
                        window.decorator &&
                          window.decorator.isCloseBtnVisible &&
                          a().createElement(
                            Gt,
                            { body: R.strings.dialogs.common.error.cancel() },
                            a().createElement("div", {
                              className: Ir.closeBtn,
                              onClick: _,
                              onMouseEnter: h,
                              ref: c,
                            }),
                          ),
                      ),
                      a().createElement("div", { className: A, style: n.arrow }),
                    ),
                  )
                );
              },
            ),
            [
              "contentId",
              "decoratorId",
              "direction",
              "targetId",
              "args",
              "onClick",
              "children",
              "isEnabled",
            ]);
        function zr() {
          return (
            (zr =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            zr.apply(this, arguments)
          );
        }
        const Ur = (e) => {
          let t = e.contentId,
            u = e.decoratorId,
            n = e.direction,
            r = void 0 === n ? Wr.Top : n,
            i = e.targetId,
            l = e.args,
            s = e.onClick,
            c = e.children,
            d = e.isEnabled,
            m = void 0 === d || d,
            E = (function (e, t) {
              if (null == e) return {};
              var u,
                n,
                r = {},
                o = Object.keys(e);
              for (n = 0; n < o.length; n++) ((u = o[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
              return r;
            })(e, Yr);
          const _ = (0, o.useRef)(null),
            h = (0, o.useCallback)(() => {
              if ((0, V.wU)()) return (0, V.SW)();
              _.current && (0, V.P3)(t, r, _.current, u, i, l);
            }, [t, r, l, u, i]);
          return a().createElement(
            "div",
            zr(
              {
                ref: _,
                onClick:
                  ((A = c.props.onClick),
                  (e) => {
                    m && (h(), s && s(e), A && A(e));
                  }),
              },
              E,
            ),
            c,
          );
          var A;
        };
        let Gr, jr, Vr, $r;
        (!(function (e) {
          e.customizationResourceExchangeScreen = "customization_resource_exchange_screen";
        })(Gr || (Gr = {})),
          (function (e) {
            e.customizationResourceSlectAll = "customization_resource_select_all";
          })(jr || (jr = {})),
          (function (e) {
            e.Click = "click";
          })(Vr || (Vr = {})),
          (function (e) {
            ((e[(e.NonSet = 0)] = "NonSet"),
              (e[(e.Debug = 10)] = "Debug"),
              (e[(e.Info = 20)] = "Info"),
              (e[(e.Warning = 30)] = "Warning"));
          })($r || ($r = {})));
        let qr;
        !(function (e) {
          ((e.Click = "click"), (e.KeyDown = "keydown"));
        })(qr || (qr = {}));
        const Kr = "metrics",
          Qr = ({ partnerID: e, item: t, parentScreen: u, itemState: n, info: r }) => ({
            item: t,
            partnerID: e || null,
            parent_screen: u || null,
            item_state: n || null,
            additional_info: r || null,
          }),
          Zr = (e, t) => {
            const u = (0, o.useCallback)(
              (u, n = $r.Info, r) => {
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
          Jr = {
            base: "NumberRange_base_83",
            base__animation: "NumberRange_base__animation_26",
            blinkAnim: "NumberRange_blinkAnim_39",
            from: "NumberRange_from_8c",
            from__red: "NumberRange_from__red_59",
            separatorWrapper: "NumberRange_separatorWrapper_33",
            separator: "NumberRange_separator_86",
            counterGlow: "NumberRange_counterGlow_7b",
          },
          eo = R.strings.crew.barracks.berthsAmountDivider(),
          to = R.strings.crew.filterPanel.counter.selectLimit,
          uo = (0, o.memo)(function ({
            isFilterRange: e,
            from: t,
            to: u,
            className: n,
            isSelectMode: r = !1,
            isSelectedLimitReached: o = !1,
            isHideTotalCounter: i = !1,
            counterGlowShift: l,
            classNames: s,
            isAnimationEnabled: c = !1,
          }) {
            const d = l
              ? a().createElement(
                  "div",
                  { className: Jr.separatorWrapper },
                  a().createElement(St, { className: Jr.separator, text: eo }),
                  a().createElement("div", {
                    style: l,
                    className: f()(
                      Jr.counterGlow,
                      o && Jr.blink,
                      null == s ? void 0 : s.counterGlow,
                    ),
                  }),
                )
              : a().createElement(St, { className: Jr.separator, text: eo });
            return r
              ? a().createElement(
                  Gt,
                  { header: to.header(), body: to.body(), ignoreShowDelay: !0 },
                  a().createElement(
                    "div",
                    { className: f()(Jr.base, n) },
                    a().createElement(St, { className: Jr.from, text: String(t) }),
                    (t !== u || o) &&
                      a().createElement(
                        a().Fragment,
                        null,
                        d,
                        a().createElement(St, { text: String(u) }),
                      ),
                  ),
                )
              : a().createElement(
                  "div",
                  {
                    className: f()(
                      Jr.base,
                      e ? 0 === t && Jr.base__animation : t > u && Jr.base__animation,
                      c && Jr.base__animation,
                      n,
                    ),
                  },
                  a().createElement(St, {
                    className: f()(
                      Jr.from,
                      e ? 0 === t && u > 0 && Jr.from__red : t > u && Jr.from__red,
                    ),
                    text: String(t),
                  }),
                  (!i || t !== u) &&
                    a().createElement(
                      a().Fragment,
                      null,
                      d,
                      a().createElement(St, { text: String(u) }),
                    ),
                );
          }),
          no = "NumberRangeWithLabel_base_db",
          ro = "NumberRangeWithLabel_counterGlow_b1",
          oo = "NumberRangeWithLabel_blink_58",
          ao = (0, o.memo)(
            ({
              title: e,
              label: t = "",
              isGlowVisible: u = !1,
              isSelectedLimitReached: n = !1,
              isFilterRange: r = !1,
              isSelectMode: i = !1,
              className: s,
              classNames: c,
              from: d,
              to: m,
              staticCounterGlowShift: E,
              isHideTotalCounter: _ = !1,
              isAnimationEnabled: h = !1,
            }) => {
              const A = (() => {
                  const e = (0, o.useState)(l.O.view.getScale()),
                    t = e[0],
                    u = e[1];
                  return (
                    (0, o.useEffect)(() => {
                      const e = () => {
                        u(l.O.view.getScale());
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
                })(),
                p =
                  d !== m || n
                    ? 7 * String(d).length * A + 4 * A
                    : Math.round((7 * String(d).length * A) / 2),
                g = { left: E || p };
              return a().createElement(
                "div",
                { className: f()(no, s) },
                t,
                a().createElement(uo, {
                  isFilterRange: r,
                  isSelectedLimitReached: n,
                  isSelectMode: i,
                  from: d,
                  to: m,
                  isHideTotalCounter: _,
                  classNames: c,
                  isAnimationEnabled: h,
                }),
                u &&
                  r &&
                  a().createElement("div", {
                    style: g,
                    className: f()(ro, n && oo, null == c ? void 0 : c.counterGlow),
                  }),
                e,
              );
            },
          ),
          io = "FilterBlock_base_2f",
          lo = "FilterBlock_filterStateHolder_86",
          so = "FilterBlock_filterCounter_6a",
          co = "FilterBlock_filterNumbers_ae",
          mo = "FilterBlock_filterNumbersLabel_77",
          Eo = "FilterBlock_counterGlow_32",
          _o = "FilterBlock_filtersClearButton_de",
          ho = "FilterBlock_filtersClearIcon_38",
          Ao = "FilterBlock_divider_af",
          po = "FilterBlock_filterButton_2e",
          go = "FilterBlock_filterIcon_f6",
          bo = R.strings.customization.tooltips.filters,
          Co = R.strings.event.customizationResource.mainView,
          Fo = (0, Xt.Pi)(() => {
            const e = An(),
              t = e.controls,
              u = e.model,
              n = u.root.get(),
              r = n.isAllSelected,
              i = n.isFilteringActive,
              l = n.filteredItemsCounter,
              s = n.allItemsCounter,
              c = n.isLimitReached,
              d = n.noAvailableItems,
              m = u.computes.getSelectedTab(),
              E = !d && c && 0 === (null == m ? void 0 : m.selectedCount),
              _ = r && !E,
              h = (0, o.useRef)(null),
              A = y().mediaSize,
              p = ((e) => {
                const t = Zr(e, Kr),
                  u = (0, o.useCallback)(
                    (e) => {
                      t(e.action, e.logLevel, Qr(e));
                    },
                    [t],
                  );
                return (e) => u(e);
              })("customization_resource"),
              g = R.strings.event.customizationResource.checkbox.tooltip.$dyn(
                (null == m ? void 0 : m.itemType) || "",
              ),
              b = (0, o.useMemo)(() => E || (!r && d), [r, d, E]),
              C = (0, o.useMemo)(
                () =>
                  b && d
                    ? Co.tooltips.noItems.body()
                    : E
                      ? Co.tooltips.limitReached.body()
                      : ot(Co.tooltips.selectAll.body(), { category: g }),
                [E, b, d, g],
              ),
              F = (0, o.useMemo)(
                () => ({
                  header: b
                    ? Co.tooltips.limitReached.header()
                    : ot(Co.tooltips.selectAll.header(), { category: g }),
                  body: C,
                  alert: b ? void 0 : Co.tooltips.selectAll.alert(),
                }),
                [b, g, C],
              ),
              D = (0, o.useCallback)(() => {
                (t.selectAll(),
                  p({
                    item: jr.customizationResourceSlectAll,
                    action: Vr.Click,
                    parentScreen: Gr.customizationResourceExchangeScreen,
                    info: JSON.stringify({
                      itemType: null == m ? void 0 : m.itemType,
                      availableCount: null == m ? void 0 : m.availableCount,
                    }),
                  }));
              }, [t, p, m]);
            return a().createElement(
              "div",
              { className: io, ref: h },
              a().createElement(
                "div",
                { className: lo },
                a().createElement(
                  "div",
                  { className: so },
                  a().createElement(ao, {
                    title:
                      i &&
                      a().createElement(
                        Gt,
                        { body: Co.filters.resetFilter() },
                        a().createElement(
                          j,
                          { type: z.ghost, onClick: t.clearFilter, mixClass: f()(_o) },
                          a().createElement("div", { className: ho }),
                        ),
                      ),
                    label: a().createElement(St, {
                      text: Co.filters.selectedTitle(),
                      className: mo,
                    }),
                    from: l,
                    to: s,
                    isFilterRange: !0,
                    isGlowVisible: i,
                    isSelectMode: !1,
                    className: co,
                    classNames: { counterGlow: Eo },
                    isHideTotalCounter: !i,
                  }),
                ),
                a().createElement("div", { className: Ao }),
                a().createElement(
                  Gt,
                  F,
                  a().createElement(
                    "div",
                    null,
                    a().createElement(Or, {
                      type: Rr.main,
                      size: Mr.large,
                      isChecked: _,
                      contentStyles: b ? { color: "#595950" } : void 0,
                      isDisabled: b,
                      onClick: D,
                      alignment: kr.Center,
                      text: _ ? Co.cancelSelect() : ot(Co.selectAll(), { category: g }),
                      soundHover: R.sounds.highlight(),
                      soundClick: R.sounds.play(),
                    }),
                  ),
                ),
              ),
              a().createElement(
                Ur,
                {
                  contentId:
                    R.views.lobby.customization_resource.CustomizationResourceFilterPopoverView(
                      "resId",
                    ),
                  direction: A < B.Small ? Wr.Left : Wr.Top,
                },
                a().createElement(
                  Gt,
                  { header: bo.popoverButtonTitle(), body: bo.popoverButtonBody() },
                  a().createElement(
                    j,
                    { type: z.ghost, size: U.small, mixClass: po },
                    a().createElement("div", { className: go }),
                  ),
                ),
              ),
            );
          });
        function fo() {
          return (
            (fo =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            fo.apply(this, arguments)
          );
        }
        const Do = R.strings.event.customizationResource.mainView,
          vo = (0, Xt.Pi)(() => {
            const e = An(),
              t = e.controls,
              u = e.model,
              n = u.computes.getItems(),
              r = u.computes.getTabs(),
              i = u.root.get(),
              l = i.selectedCount,
              s = i.exchangeReward,
              c = i.currencyBalance,
              d = i.isExchangeConfirmationVisible,
              m = i.isAllItemsHiddenByFilter,
              E = i.limit,
              _ = i.isLimitReached,
              h = ze.Vertical.useVerticalScrollApi(),
              A = h.getWrapperSize(),
              p = h.getContainerSize(),
              g = (0, o.useRef)(new Map()),
              b = ne(
                (e, t, u, n) => {
                  if (t) {
                    var r;
                    let o = 0,
                      a = u,
                      i = !1,
                      l = 0;
                    for (; l < u;) {
                      const u = n(l);
                      if (u) {
                        const n = u.position - e < 0,
                          r = u.position - e > t;
                        if ((n && l > o ? (o = l) : i || (i = !u.isFilled), r)) {
                          a = l;
                          break;
                        }
                      }
                      l++;
                    }
                    i || (i = !(null != (r = n(o)) && r.isFilled));
                    let s = o,
                      c = 0;
                    for (; c < 5 && s > 0;) (s--, c++);
                    ((o = s), i && C(o, a));
                  }
                },
                [(C = t.loadCards)],
                200,
              );
            var C;
            const F = (0, o.useState)([0, 0]),
              D = F[0],
              v = F[1],
              w = { top: D[0], bottom: D[1] },
              S = w.top <= 0 && w.bottom <= 0,
              x = (0, o.useCallback)(() => {
                const e = h.getBounds(),
                  t = e[0],
                  u = e[1];
                (t === w.top && u === w.bottom) || v([t, u]);
              }, [h, w.top, w.bottom]),
              T = (0, o.useCallback)(
                (e) => {
                  const t = n[e],
                    u = g.current.get(t.intCD);
                  if (u) return { position: u.offsetTop, isFilled: t.isFilled };
                },
                [n],
              ),
              L = (0, o.useCallback)(() => {
                const e = h.getWrapperSize();
                if (e) {
                  const t = h.animationScroll.scrollPosition.goal;
                  b(t, e, n.length, T);
                }
              }, [h, n.length, b, T]),
              M = (0, o.useCallback)(() => {
                (x(), L());
              }, [x, L]);
            (It({ callback: t.onClose, preventPropagation: !1 }),
              (0, o.useEffect)(
                () => (
                  h.events.on("change", M),
                  h.events.on("recalculateContent", M),
                  h.events.on("resizeHandled", M),
                  () => {
                    (h.events.off("change", M),
                      h.events.off("recalculateContent", M),
                      h.events.off("resizeHandled", M));
                  }
                ),
                [M, x, h.events],
              ));
            const k = (0, o.useState)(-1),
              N = k[0],
              P = k[1];
            (Wt(() => {
              if (N > -1 && A && p && !S) {
                const e = g.current.get(N);
                if (e) {
                  const t = e.offsetTop - 0.5 * e.offsetHeight;
                  (h.applyScroll(t, { immediate: !0, reset: !0 }), P(-1));
                }
              }
            }, [A, p, S, h]),
              Wt(() => {
                h.applyScroll(0, { immediate: !0, reset: !0 });
              }, [h]));
            const O = (0, o.useCallback)(
                (e) => {
                  (W(R.sounds.cust_tab_switch()), t.selectTab(e));
                },
                [t],
              ),
              H = (0, o.useCallback)(
                (e, u) => {
                  e && t.onAdd(e, u);
                },
                [t],
              ),
              I = (0, o.useCallback)(
                (e, u) => {
                  e && t.onReduce(e, u);
                },
                [t],
              ),
              X = y().mediaSize <= B.Small ? U.small : U.medium,
              Y = (0, o.useMemo)(() => f()(pn.scrollArea, S && pn.scrollArea__withoutScroll), [S]),
              G = (0, o.useMemo)(
                () => ({ content: f()(pn.scrollContent, S && pn.scrollContent__withoutScroll) }),
                [S],
              );
            return a().createElement(
              "div",
              { className: pn.base },
              a().createElement(
                "div",
                { className: pn.header },
                a().createElement(St, { className: pn.title, text: Do.title() }),
                a().createElement(St, { className: pn.subTitle, text: Do.subTitle() }),
              ),
              a().createElement(
                "div",
                { className: pn.categories },
                a().createElement("div", { className: pn.categoriesBackground }),
                r.map((e, t) =>
                  a().createElement(
                    "div",
                    { key: `${t}_${e.tabId}`, className: pn.category },
                    a().createElement(un, fo({}, e, { tabId: e.tabId, onClick: O })),
                    t !== r.length - 1 && a().createElement("div", { className: pn.divider }),
                  ),
                ),
              ),
              a().createElement("div", { className: pn.filters }, a().createElement(Fo, null)),
              a().createElement(
                "div",
                { className: pn.carouselWrapper },
                m &&
                  a().createElement(
                    uu,
                    {
                      warningHeader: Do.filters.emptyTitle(),
                      warningDescription: Do.filters.emptyDescription(),
                      buttonType: z.secondary,
                      onClick: t.clearFilter,
                      className: pn.emptyState,
                    },
                    a().createElement(St, { text: Do.resetFiltersBtn.label() }),
                  ),
                !m &&
                  n &&
                  n.length > 0 &&
                  a().createElement(
                    a().Fragment,
                    null,
                    a().createElement(
                      ze.Vertical.Area,
                      { api: h, className: Y, classNames: G },
                      a().createElement(
                        "div",
                        { className: pn.itemsHolder },
                        n.map((e) =>
                          a().createElement(
                            "div",
                            {
                              key: e.intCD,
                              className: pn.reward,
                              ref: (t) => {
                                t ? g.current.set(e.intCD, t) : g.current.delete(e.intCD);
                              },
                            },
                            a().createElement(
                              Wu,
                              fo({}, e, { isLimitReached: _, limit: E, onAdd: H, onReduce: I }),
                            ),
                          ),
                        ),
                      ),
                    ),
                    a().createElement(
                      "div",
                      { className: pn.scrollbarWrapper },
                      a().createElement(ze.Vertical.Bar, {
                        classNames: { thumb: pn.thumb },
                        api: h,
                      }),
                    ),
                  ),
              ),
              a().createElement(
                Nt,
                {
                  contentId:
                    R.views.lobby.customization_resource.tooltips.CustomizationResourceCurrencyTooltipView(
                      "resId",
                    ),
                },
                a().createElement(
                  "div",
                  { className: pn.currency },
                  a().createElement(
                    "div",
                    { className: pn.paintsHolder },
                    a().createElement("div", { className: pn.paintsIcon }),
                    a().createElement(
                      "div",
                      { className: pn.paintsBalance },
                      a().createElement($, { value: c }),
                    ),
                  ),
                ),
              ),
              a().createElement(
                "div",
                { className: pn.closeButton },
                a().createElement(Lt, {
                  side: "right",
                  type: "close",
                  caption: Do.closeButton(),
                  onClick: t.onClose,
                }),
              ),
              a().createElement(
                "div",
                { className: pn.aboutButton },
                a().createElement(Lt, {
                  caption: R.strings.resource_well.commonTexts.aboutButton(),
                  type: "info",
                  onClick: t.onShowInfo,
                }),
              ),
              a().createElement(
                "div",
                { className: pn.priceWrapper },
                a().createElement(
                  "div",
                  { className: pn.price },
                  a().createElement(
                    "div",
                    { className: pn.exchangeText },
                    0 === l
                      ? a().createElement(St, { text: Do.exchangeDisableText() })
                      : a().createElement(
                          a().Fragment,
                          null,
                          a().createElement(St, {
                            text: Do.exchangeSelectedText(),
                            className: pn.exchangeEnableText,
                          }),
                          a().createElement(St, {
                            text: Do.counter(),
                            className: pn.limitsHolder,
                            format: {
                              binding: {
                                selectedCount: a().createElement(
                                  "div",
                                  { className: pn.paintsTotal },
                                  a().createElement($, { value: l }),
                                ),
                                availableCount: a().createElement($, { value: E }),
                              },
                            },
                          }),
                          a().createElement(St, {
                            text: Do.exchangeEnableText(),
                            className: pn.exchangeEnableText,
                          }),
                          a().createElement(
                            Nt,
                            {
                              contentId:
                                R.views.lobby.customization_resource.tooltips.CustomizationResourceCurrencyTooltipView(
                                  "resId",
                                ),
                            },
                            a().createElement(
                              "div",
                              { className: pn.currencyHolder },
                              a().createElement(
                                "div",
                                { className: pn.paintsTotal },
                                a().createElement($, { value: s }),
                              ),
                              a().createElement("div", { className: pn.paintsIcon }),
                            ),
                          ),
                        ),
                  ),
                  a().createElement(
                    j,
                    {
                      type: z.primary,
                      size: X,
                      mixClass: pn.exchangeButton,
                      disabled: 0 === l,
                      onClick: t.onExchange,
                    },
                    a().createElement(St, { text: Do.exchangeButton() }),
                  ),
                ),
                a().createElement(St, {
                  text: Do.limitText(),
                  className: pn.limitText,
                  format: { binding: { limit: a().createElement($, { value: E }) } },
                }),
              ),
              d && a().createElement(xr, null),
            );
          });
        engine.whenReady.then(() => {
          I().render(
            a().createElement(hn, null, a().createElement(O, null, a().createElement(vo, null))),
            document.getElementById("root"),
          );
        });
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
        var r = 1 / 0;
        for (l = 0; l < deferred.length; l++) {
          for (var [t, u, n] = deferred[l], o = !0, a = 0; a < t.length; a++)
            (!1 & n || r >= n) &&
            Object.keys(__webpack_require__.O).every((e) => __webpack_require__.O[e](t[a]))
              ? t.splice(a--, 1)
              : ((o = !1), n < r && (r = n));
          if (o) {
            deferred.splice(l--, 1);
            var i = u();
            void 0 !== i && (e = i);
          }
        }
        return e;
      }
      n = n || 0;
      for (var l = deferred.length; l > 0 && deferred[l - 1][2] > n; l--)
        deferred[l] = deferred[l - 1];
      deferred[l] = [t, u, n];
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
    (__webpack_require__.j = 766),
    (() => {
      var e = { 766: 0 };
      __webpack_require__.O.j = (t) => 0 === e[t];
      var t = (t, u) => {
          var n,
            r,
            [o, a, i] = u,
            l = 0;
          if (o.some((t) => 0 !== e[t])) {
            for (n in a) __webpack_require__.o(a, n) && (__webpack_require__.m[n] = a[n]);
            if (i) var s = i(__webpack_require__);
          }
          for (t && t(u); l < o.length; l++)
            ((r = o[l]), __webpack_require__.o(e, r) && e[r] && e[r][0](), (e[r] = 0));
          return __webpack_require__.O(s);
        },
        u = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (u.forEach(t.bind(null, 0)), (u.push = t.bind(null, u.push.bind(u))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [841], () => __webpack_require__(409));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
