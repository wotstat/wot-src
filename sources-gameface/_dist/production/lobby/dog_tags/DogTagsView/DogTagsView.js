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
        function a(e, t) {
          if (!r) throw new Error("No element matching method supported");
          return r.call(e, t);
        }
        function o(e) {
          e.remove ? e.remove() : e.parentNode && e.parentNode.removeChild(e);
        }
        function i(e, t) {
          return Array.prototype.filter.call(e.children, function (e) {
            return a(e, t);
          });
        }
        var s = "ps",
          l = {
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
        var g = function (e) {
            ((this.element = e), (this.handlers = {}));
          },
          A = { isEmpty: { configurable: !0 } };
        ((g.prototype.bind = function (e, t) {
          (void 0 === this.handlers[e] && (this.handlers[e] = []),
            this.handlers[e].push(t),
            this.element.addEventListener(e, t, !1));
        }),
          (g.prototype.unbind = function (e, t) {
            var u = this;
            this.handlers[e] = this.handlers[e].filter(function (n) {
              return !(!t || n === t) || (u.element.removeEventListener(e, n, !1), !1);
            });
          }),
          (g.prototype.unbindAll = function () {
            for (var e in this.handlers) this.unbind(e);
          }),
          (A.isEmpty.get = function () {
            var e = this;
            return Object.keys(this.handlers).every(function (t) {
              return 0 === e.handlers[t].length;
            });
          }),
          Object.defineProperties(g.prototype, A));
        var h = function () {
          this.eventElements = [];
        };
        function p(e) {
          return parseInt(e, 10) || 0;
        }
        ((h.prototype.eventElement = function (e) {
          var t = this.eventElements.filter(function (t) {
            return t.element === e;
          })[0];
          return (t || ((t = new g(e)), this.eventElements.push(t)), t);
        }),
          (h.prototype.bind = function (e, t, u) {
            this.eventElement(e).bind(t, u);
          }),
          (h.prototype.unbind = function (e, t, u) {
            var n = this.eventElement(e);
            (n.unbind(t, u),
              n.isEmpty && this.eventElements.splice(this.eventElements.indexOf(n), 1));
          }),
          (h.prototype.unbindAll = function () {
            (this.eventElements.forEach(function (e) {
              return e.unbindAll();
            }),
              (this.eventElements = []));
          }),
          (h.prototype.once = function (e, t, u) {
            var n = this.eventElement(e);
            n.bind(t, function e(r) {
              (n.unbind(t, e), u(r));
            });
          }));
        var F = {
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
        function b() {
          return new Promise(function (e) {
            requestAnimationFrame(function () {
              requestAnimationFrame(function () {
                e();
              });
            });
          });
        }
        function D(e) {
          if ("function" == typeof window.CustomEvent) return new CustomEvent(e);
          var t = document.createEvent("CustomEvent");
          return (t.initCustomEvent(e, !1, !1, void 0), t);
        }
        var v = function (e, t, u, n, r, a) {
          var o;
          if (
            (void 0 === n && (n = !0),
            void 0 === r && (r = !1),
            void 0 === a && (a = !1),
            "top" === t)
          )
            o = ["contentHeight", "containerHeight", "scrollTop", "y", "up", "down"];
          else {
            if ("left" !== t) throw new Error("A proper axis should be provided");
            o = ["contentWidth", "containerWidth", "scrollLeft", "x", "left", "right"];
          }
          !(function (e, t, u, n, r, a) {
            var o = u[0],
              i = u[1],
              s = u[2],
              l = u[3],
              c = u[4],
              d = u[5];
            void 0 === n && (n = !0);
            void 0 === r && (r = !1);
            void 0 === a && (a = !1);
            var m = e.element;
            if (!e.reach) return;
            ((e.reach[l] = null), m[s] < 1 && (e.reach[l] = "start"));
            m[s] > e[o] - e[i] - 1 && (e.reach[l] = "end");
            t &&
              !r &&
              (m.dispatchEvent(D("ps-scroll-" + l)),
              t < 0
                ? m.dispatchEvent(D("ps-scroll-" + c))
                : t > 0 && m.dispatchEvent(D("ps-scroll-" + d)),
              n &&
                (function (e, t) {
                  (E(e, t), _(e, t));
                })(e, l));
            e.reach[l] && (t || a) && m.dispatchEvent(D("ps-" + l + "-reach-" + e.reach[l]));
          })(e, u, o, n, r, a);
        };
        var C = function (e, t, n, r) {
          (void 0 === t && (t = !1), void 0 === n && (n = 0), void 0 === r && (r = !1));
          var a = e.element;
          if (a) {
            if (
              ((e.containerWidth = Math.round(a.getBoundingClientRect().width)),
              (e.containerHeight = Math.round(a.getBoundingClientRect().height)),
              (e.contentWidth = Math.round(a.scrollWidth) - 2 * n),
              (e.contentHeight = Math.round(a.scrollHeight)),
              !r)
            ) {
              e.contentWidth = Math.round(a.scrollWidth) - 2 * n;
              var s = e.contentWidth - e.containerWidth + n;
              a.scrollLeft < n ? (a.scrollLeft = n) : a.scrollLeft > s && (a.scrollLeft = s);
            }
            var d = Math.floor(a.scrollTop),
              m = Math.floor(a.scrollLeft) - n,
              E = parseFloat(getComputedStyle(document.documentElement).fontSize);
            (a.contains(e.scrollbarXRail) ||
              (i(a, l.rail("x")).forEach(function (e) {
                return o(e);
              }),
              a.appendChild(e.scrollbarXRail)),
              a.contains(e.scrollbarYRail) ||
                (i(a, l.rail("y")).forEach(function (e) {
                  return o(e);
                }),
                a.appendChild(e.scrollbarYRail)),
              !e.settings.suppressScrollX &&
              e.containerWidth + e.settings.scrollXMarginOffset < e.contentWidth
                ? ((e.scrollbarXActive = !0),
                  (e.railXWidth = e.containerWidth - e.railXMarginWidth * E - 15 * E),
                  (e.railXRatio = e.containerWidth / e.railXWidth),
                  (e.scrollbarXWidth = f(e, p((e.railXWidth * e.containerWidth) / e.contentWidth))),
                  (e.scrollbarXLeft = p(
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
                  (e.scrollbarYHeight = f(
                    e,
                    p((e.railYHeight * e.containerHeight) / e.contentHeight),
                  )),
                  (e.scrollbarYTop = p(
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
                  a = Math.floor(e.scrollTop);
                t.isRtl
                  ? (r.left =
                      t.negativeScrollAdjustment + e.scrollLeft + t.containerWidth - t.contentWidth)
                  : (r.left = e.scrollLeft);
                t.isScrollbarXUsingBottom
                  ? (r.bottom = t.scrollbarXBottom - a)
                  : (r.top = t.scrollbarXTop + a);
                u(t.scrollbarXRail, r);
                var o = { top: a, height: t.railYHeight };
                t.isScrollbarYUsingRight
                  ? t.isRtl
                    ? (o.right =
                        t.contentWidth -
                        (t.negativeScrollAdjustment + e.scrollLeft) -
                        t.scrollbarYRight -
                        t.scrollbarYOuterWidth)
                    : (o.right = t.scrollbarYRight - e.scrollLeft)
                  : t.isRtl
                    ? (o.left =
                        t.negativeScrollAdjustment +
                        e.scrollLeft +
                        2 * t.containerWidth -
                        t.contentWidth -
                        t.scrollbarYLeft -
                        t.scrollbarYOuterWidth)
                    : (o.left = t.scrollbarYLeft + e.scrollLeft);
                (u(t.scrollbarYRail, o),
                  u(t.scrollbarX, {
                    left: t.scrollbarXLeft,
                    width: t.scrollbarXWidth - t.railBorderXWidth * n,
                  }),
                  u(t.scrollbarY, {
                    top: t.scrollbarYTop,
                    height: t.scrollbarYHeight - t.railBorderYWidth * n,
                  }));
              })(a, e, E),
              e.scrollbarXButtonStart.classList.toggle("disabled", m < 1),
              e.scrollbarXButtonEnd.classList.toggle(
                "disabled",
                m + e.containerWidth >= e.contentWidth,
              ),
              e.scrollbarYButtonStart.classList.toggle("disabled", a.scrollTop < 1),
              e.scrollbarYButtonEnd.classList.toggle(
                "disabled",
                a.scrollTop + e.containerHeight >= e.contentHeight,
              ),
              e.scrollbarXActive
                ? (a.classList.add(c.active("x")), v(e, "left", m - e.lastScrollLeft, !0, t))
                : (a.classList.remove(c.active("x")),
                  (e.scrollbarXWidth = 0),
                  (e.scrollbarXLeft = 0),
                  (a.scrollLeft = 0)),
              e.scrollbarYActive
                ? (a.classList.add(c.active("y")),
                  v(e, "top", a.scrollTop - e.lastScrollTop, !0, t))
                : (a.classList.remove(c.active("y")),
                  (e.scrollbarYHeight = 0),
                  (e.scrollbarYTop = 0),
                  (a.scrollTop = 0)),
              (e.lastScrollTop = d),
              (e.lastScrollLeft = m),
              (e.scrollTopPercent = a.scrollTop / a.scrollHeight),
              (e.scrollLeftPercent = a.scrollLeft / a.scrollWidth));
          }
        };
        function f(e, t) {
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
              a = e.x2,
              o = e.y2;
            return (
              1 -
              (n * ((t = u), Math.pow(t, 3)) +
                r *
                  (function (e) {
                    return 3 * e * e * (1 - e);
                  })(u) +
                a *
                  (function (e) {
                    return 3 * e * Math.pow(1 - e, 2);
                  })(u) +
                o *
                  (function (e) {
                    return Math.pow(1 - e, 3);
                  })(u))
            );
          },
          y = { breakBounds: !1, startBound: 0, endBound: 0 },
          S = function (e) {
            var t = e.scrollableDomEle,
              u = e.onAnimationCompleteCallback,
              n = e.direction,
              r = e.onRefUpdateCallback,
              a = e.duration,
              o = e.cubicBezierPoints,
              i = e.easingPreset,
              s = e.scrollAmount,
              l = e.onCheckForBreakCallback,
              c = e.boundsInfo;
            void 0 === c && (c = y);
            var d = null,
              m = null,
              E = null,
              _ = null,
              g = t === window,
              A = ["left", "right"].indexOf(n) > -1,
              h = ["right", "bottom"].indexOf(n) > -1;
            A
              ? ((m = g ? "scrollX" : "scrollLeft"),
                (_ = g ? "innerWidth" : "width"),
                (E = "scrollWidth"))
              : ((m = g ? "scrollY" : "scrollTop"),
                (_ = g ? "innerHeight" : "height"),
                (E = "scrollHeight"));
            var p = t[m],
              F = (function (e) {
                var t,
                  u = e.isWindow,
                  n = e.scrollableDomEle,
                  r = e.elementLengthProp,
                  a = e.initialScrollPosition,
                  o = e.isHorizontalDirection,
                  i = e.scrollLengthProp,
                  s = e.direction;
                if (u) {
                  var l = document.documentElement;
                  t = o ? l.offsetWidth : l.offsetHeight;
                } else t = (n[i] - n.getBoundingClientRect()[r]) | 0;
                return ["left", "top"].includes(s) ? a : t - a;
              })({
                isWindow: g,
                scrollableDomEle: t,
                elementLengthProp: _,
                initialScrollPosition: p,
                isHorizontalDirection: A,
                scrollLengthProp: E,
                direction: n,
              });
            !isNaN(s) && s < F && (F = s);
            var b = function e(n) {
              if (!l || !l()) {
                var s = n - d,
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
                  })({ easingPreset: i, cubicBezierPoints: o, runTime: s, duration: a });
                if (!isNaN(E)) {
                  var _ = Math.round(E * F),
                    b = h ? _ + p : F - _;
                  if (
                    (c.breakBounds &&
                      (b < c.startBound ? (b = c.startBound) : b > c.endBound && (b = c.endBound)),
                    s < a)
                  ) {
                    if (g) {
                      var D = A ? b : 0,
                        v = A ? 0 : b;
                      window.scrollTo(D, v);
                    } else t[m] = b;
                    (r && r(b), requestAnimationFrame(e));
                  } else u && u();
                }
              }
            };
            requestAnimationFrame(function (e) {
              ((d = e), b(e));
            });
          },
          k = function (e) {
            var t = e.axis,
              u = e.cursorPositionOnRail,
              n = e.direction,
              r = e.i,
              a = (function (e) {
                var t = e.axis,
                  u = e.i,
                  n = e.cursorPositionOnRail;
                if ("y" === t) {
                  var r = u.scrollbarY.offsetTop,
                    a = r + u.scrollbarYHeight;
                  return n >= r && n <= a;
                }
                var o = u.scrollbarX.offsetLeft,
                  i = o + u.scrollbarXWidth;
                return n >= o && n <= i;
              })({ axis: t, i: r, cursorPositionOnRail: u });
            return a
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
                    a = (n - r.scrollbar / 2) / r.rail,
                    o = Math.round(Math.min(r.maxScroll, Math.max(0, r.content * a)));
                  "y" === t ? (u.element.scrollTop = o) : (u.element.scrollLeft = o);
                })({ axis: t, i: r, cursorPositionOnRail: u }),
                !0)
              : ("y" === t
                  ? (r.element.scrollTop += n * r.containerHeight)
                  : (r.element.scrollLeft += n * r.containerWidth),
                !1);
          },
          x = function (e, t, u) {
            return function (n) {
              t = t.toLowerCase();
              var r = null,
                a = function () {
                  if (1 === n.buttons) {
                    if (
                      !n.target.closest(".ps__rail-" + t) ||
                      !n.target.closest(".ps__track_" + t)
                    ) {
                      var a = (function (e) {
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
                        o = a.cursorPosition - a.windowScrolled - a.elementPosition,
                        i = (function (e) {
                          var t = e.axis,
                            u = e.cursorPositionOnRail,
                            n = e.i;
                          return u > ("y" === t ? n.scrollbarYTop : n.scrollbarXLeft) ? 1 : -1;
                        })({ axis: t, cursorPositionOnRail: o, i: e });
                      (k({ axis: t, cursorPositionOnRail: o, direction: i, i: e }) &&
                        clearTimeout(r),
                        C(e, !1, u));
                    }
                    n.stopPropagation();
                  }
                };
              (a(),
                (r = setInterval(a, 100)),
                e.event.once(e.ownerDocument, "mouseup", function () {
                  clearTimeout(r);
                }));
            };
          };
        function L(e, t, u) {
          var n = u[0],
            r = u[1],
            a = u[2],
            o = u[3],
            i = u[4],
            s = u[5],
            l = u[6],
            d = u[7],
            m = u[8],
            g = e.element,
            A = null,
            h = null,
            F = null;
          function b(u) {
            ((g[l] = p(A + F * (u[a] - h))),
              E(e, d),
              C(e, !1, t),
              u.stopPropagation(),
              u.preventDefault());
          }
          function D() {
            (_(e, d),
              e[m].classList.remove(c.clicking),
              e.event.unbind(e.ownerDocument, "mousemove", b));
          }
          e.event.bind(e[i], "mousedown", function (t) {
            1 === t.buttons &&
              ((A = g[l]),
              (h = t[a]),
              (F = (e[r] - e[n]) / (e[o] - e[s])),
              e.event.bind(e.ownerDocument, "mousemove", b),
              e.event.once(e.ownerDocument, "mouseup", D),
              e[m].classList.add(c.clicking),
              t.stopPropagation(),
              t.preventDefault());
          });
        }
        var T = 1e3,
          N = {
            "click-rail": function (e, t) {
              (e.event.bind(e.scrollbarY, "mousedown", function (e) {
                return e.stopPropagation();
              }),
                e.event.bind(e.scrollbarYRail, "mousedown", x(e, "y", 0)),
                e.event.bind(e.scrollbarX, "mousedown", function (e) {
                  return e.stopPropagation();
                }),
                e.event.bind(e.scrollbarXRail, "mousedown", x(e, "x", t)));
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
                  a(u, ":hover")
                ) {
                  var r,
                    o = document.activeElement
                      ? document.activeElement
                      : e.ownerDocument.activeElement;
                  if (o) {
                    if ("IFRAME" === o.tagName) o = o.contentDocument.activeElement;
                    else for (; o.shadowRoot;) o = o.shadowRoot.activeElement;
                    if (
                      a((r = o), "input,[contenteditable]") ||
                      a(r, "select,[contenteditable]") ||
                      a(r, "textarea,[contenteditable]") ||
                      a(r, "button,[contenteditable]")
                    )
                      return;
                  }
                  var i = 0,
                    s = 0;
                  switch (n.which) {
                    case 37:
                      i = n.metaKey ? -e.contentWidth : n.altKey ? -e.containerWidth : -30;
                      break;
                    case 38:
                      s = n.metaKey ? e.contentHeight : n.altKey ? e.containerHeight : 30;
                      break;
                    case 39:
                      i = n.metaKey ? e.contentWidth : n.altKey ? e.containerWidth : 30;
                      break;
                    case 40:
                      s = n.metaKey ? -e.contentHeight : n.altKey ? -e.containerHeight : -30;
                      break;
                    case 32:
                      s = n.shiftKey ? e.containerHeight : -e.containerHeight;
                      break;
                    case 33:
                      s = e.containerHeight;
                      break;
                    case 34:
                      s = -e.containerHeight;
                      break;
                    case 36:
                      s = e.contentHeight;
                      break;
                    case 35:
                      s = -e.contentHeight;
                      break;
                    default:
                      return;
                  }
                  (e.settings.suppressScrollX && 0 !== i) ||
                    (e.settings.suppressScrollY && 0 !== s) ||
                    ((u.scrollTop -= s),
                    (u.scrollLeft += i),
                    C(e, !1, t),
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
                      var a = u.scrollLeft;
                      if (0 === n) {
                        if (!e.scrollbarXActive) return !1;
                        if ((0 === a && t < 0) || (a >= e.contentWidth - e.containerWidth && t > 0))
                          return !e.settings.wheelPropagation;
                      }
                      return !0;
                    })(i, s) && n.preventDefault());
                }
              });
            },
            wheel: function (e, u) {
              var n = e.element;
              function r(r) {
                var a = (function (e) {
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
                  o = a[0],
                  i = a[1];
                if (
                  !(function (e, u, r) {
                    if (!F.isWebKit && n.querySelector("select")) return !0;
                    if (!n.contains(e)) return !1;
                    for (var a = e; a && a !== n;) {
                      if (a.classList.contains(l.consuming)) return !0;
                      var o = t(a);
                      if ([o.overflow, o.overflowX, o.overflowY].join("").match(/(scroll|auto)/)) {
                        var i = a.scrollHeight - a.clientHeight;
                        if (
                          i > 0 &&
                          !((0 === a.scrollTop && r > 0) || (a.scrollTop === i && r < 0))
                        )
                          return !0;
                        var s = a.scrollWidth - a.clientWidth;
                        if (
                          s > 0 &&
                          !((0 === a.scrollLeft && u < 0) || (a.scrollLeft === s && u > 0))
                        )
                          return !0;
                      }
                      a = a.parentNode;
                    }
                    return !1;
                  })(r.target, o, i)
                ) {
                  var s = !1,
                    c = (o * e.settings.wheelSpeed) | 0,
                    d = (i * e.settings.wheelSpeed) | 0;
                  (e.settings.useBothWheelAxes
                    ? e.scrollbarYActive && !e.scrollbarXActive
                      ? (i ? (n.scrollTop -= d) : (n.scrollTop += c), (s = !0))
                      : e.scrollbarXActive &&
                        !e.scrollbarYActive &&
                        (o ? (n.scrollLeft += c) : (n.scrollLeft -= d), (s = !0))
                    : ((n.scrollTop -= d), (n.scrollLeft += c)),
                    C(e, !1, u),
                    (s =
                      s ||
                      (function (t, u) {
                        var r = Math.floor(n.scrollTop),
                          a = 0 === n.scrollTop,
                          o = r + n.offsetHeight === n.scrollHeight,
                          i = 0 === n.scrollLeft,
                          s = n.scrollLeft + n.offsetWidth === n.scrollWidth;
                        return (
                          !(Math.abs(u) > Math.abs(t) ? a || o : i || s) ||
                          !e.settings.wheelPropagation
                        );
                      })(o, i)),
                    s && !r.ctrlKey && (r.stopPropagation(), r.preventDefault()));
                }
              }
              (e.event.bind(n, "wheel", r),
                void 0 !== window.onmousewheel && e.event.bind(n, "mousewheel", r));
            },
            touch: function (e, u) {
              if (F.supportsTouch || F.supportsIePointer) {
                var n = e.element,
                  r = {},
                  a = 0,
                  o = {},
                  i = null;
                F.supportsTouch
                  ? (e.event.bind(n, "touchstart", m),
                    e.event.bind(n, "touchmove", E),
                    e.event.bind(n, "touchend", _))
                  : F.supportsIePointer &&
                    (window.PointerEvent
                      ? (e.event.bind(n, "pointerdown", m),
                        e.event.bind(n, "pointermove", E),
                        e.event.bind(n, "pointerup", _))
                      : window.MSPointerEvent &&
                        (e.event.bind(n, "MSPointerDown", m),
                        e.event.bind(n, "MSPointerMove", E),
                        e.event.bind(n, "MSPointerUp", _)));
              }
              function s(t, r) {
                ((n.scrollTop -= r), (n.scrollLeft -= t), C(e, !1, u));
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
                    (a = new Date().getTime()),
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
                      for (var a = e; a && a !== n;) {
                        if (a.classList.contains(l.consuming)) return !0;
                        var o = t(a);
                        if (
                          [o.overflow, o.overflowX, o.overflowY].join("").match(/(scroll|auto)/)
                        ) {
                          var i = a.scrollHeight - a.clientHeight;
                          if (
                            i > 0 &&
                            !((0 === a.scrollTop && r > 0) || (a.scrollTop === i && r < 0))
                          )
                            return !0;
                          var s = a.scrollLeft - a.clientWidth;
                          if (
                            s > 0 &&
                            !((0 === a.scrollLeft && u < 0) || (a.scrollLeft === s && u > 0))
                          )
                            return !0;
                        }
                        a = a.parentNode;
                      }
                      return !1;
                    })(u.target, E, _)
                  )
                    return;
                  (s(E, _), (r = m));
                  var g = new Date().getTime(),
                    A = g - a;
                  (A > 0 && ((o.x = E / A), (o.y = _ / A), (a = g)),
                    (function (t, u) {
                      var r = Math.floor(n.scrollTop),
                        a = n.scrollLeft,
                        o = Math.abs(t),
                        i = Math.abs(u);
                      if (i > o) {
                        if (
                          (u < 0 && r === e.contentHeight - e.containerHeight) ||
                          (u > 0 && 0 === r)
                        )
                          return 0 === window.scrollY && u > 0 && F.isChrome;
                      } else if (
                        o > i &&
                        ((t < 0 && a === e.contentWidth - e.containerWidth) || (t > 0 && 0 === a))
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
                      : o.x || o.y
                        ? Math.abs(o.x) < 0.01 && Math.abs(o.y) < 0.01
                          ? clearInterval(i)
                          : (s(30 * o.x, 30 * o.y), (o.x *= 0.8), (o.y *= 0.8))
                        : clearInterval(i);
                  }, 10)));
              }
            },
            "drag-move": function (e, t) {
              void 0 === t && (t = 0);
              var u = e.element,
                n = null,
                r = !1,
                a = 0,
                o = 0,
                i = 0;
              function s() {
                e.onScroll();
              }
              function l(n, r, a, o) {
                (void 0 === a && (a = null),
                  void 0 === o && (o = !1),
                  S({
                    scrollableDomEle: u,
                    direction: "right",
                    onRefUpdateCallback: s,
                    duration: r,
                    easingPreset: "easeOutCubic",
                    scrollAmount: n,
                    onCheckForBreakCallback: a,
                    boundsInfo: {
                      breakBounds: o,
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
              function g(r) {
                if (e.scrollbarXActive) {
                  var s = n - r.screenX;
                  ((u.scrollLeft += s), (n = r.screenX));
                  var l = new Date().getTime();
                  if (((a = (s / (l - o)) * 1e3), (o = l), e.onScroll(), t > 0)) {
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
                  (o = new Date().getTime()));
              }
              function h(n) {
                var r = e.contentWidth - e.containerWidth + t;
                if (u.scrollLeft < t) l(t - u.scrollLeft, T, d);
                else if (u.scrollLeft > r) l(r - u.scrollLeft, T, d);
                else {
                  new Date().getTime() - o < 100 && l(a / 4, T, d, !0);
                }
                (_(e, "x"),
                  _(e, "dragging", { immediately: !0 }),
                  e.scrollbarXRail.classList.remove(c.clicking),
                  e.event.unbind(e.ownerDocument, "mousemove", g));
              }
              function p() {
                r = !0;
              }
              u.addEventListener(
                "mousedown",
                function (t) {
                  1 === t.buttons &&
                    ((n = t.screenX),
                    e.event.bind(e.ownerDocument, "mousemove", g),
                    e.event.once(e.ownerDocument, "mouseup", h),
                    e.event.once(e.ownerDocument, "mousedown", A),
                    e.event.once(u, "wheel", p),
                    e.scrollbarXRail.classList.add(c.clicking),
                    t.preventDefault());
                },
                !1,
              );
            },
          },
          R = function (e, r) {
            var a = this;
            if (
              (void 0 === r && (r = {}),
              "string" == typeof e && (e = document.querySelector(e)),
              !e || !e.nodeName)
            )
              throw new Error("no element is specified to initialize PerfectScrollbar");
            for (var o in ((this.element = e),
            e.classList.add(s),
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
              a.settings[o] = r[o];
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
              (this.event = new h()),
              (this.ownerDocument = e.ownerDocument || document),
              (this.scrollbarXRail = n(l.rail("x"))),
              (this.scrollbarXButtonStart = n(l.buttonStart("x"))),
              (this.scrollbarXButtonEnd = n(l.buttonEnd("x"))),
              (this.scrollbarXTrack = n(l.track("x"))),
              e.appendChild(this.scrollbarXRail),
              this.scrollbarXRail.appendChild(this.scrollbarXTrack),
              this.scrollbarXRail.appendChild(this.scrollbarXButtonStart),
              this.scrollbarXRail.appendChild(this.scrollbarXButtonEnd),
              (this.scrollbarX = n(l.thumb("x"))),
              this.scrollbarXRail.appendChild(this.scrollbarX),
              this.scrollbarX.setAttribute("tabindex", 0),
              this.event.bind(this.scrollbarX, "focus", m),
              this.event.bind(this.scrollbarX, "blur", E),
              (this.scrollbarXActive = null),
              (this.scrollbarXWidth = null),
              (this.scrollbarXLeft = null),
              (this.scrollbarYRail = n(l.rail("y"))),
              (this.scrollbarYButtonStart = n(l.buttonStart("y"))),
              (this.scrollbarYButtonEnd = n(l.buttonEnd("y"))),
              (this.scrollbarYTrack = n(l.track("y"))),
              e.appendChild(this.scrollbarYRail),
              this.scrollbarYRail.appendChild(this.scrollbarYTrack),
              this.scrollbarYRail.appendChild(this.scrollbarYButtonStart),
              this.scrollbarYRail.appendChild(this.scrollbarYButtonEnd),
              (this.scrollbarY = n(l.thumb("y"))),
              this.scrollbarYRail.appendChild(this.scrollbarY),
              this.scrollbarY.setAttribute("tabindex", 0),
              this.event.bind(this.scrollbarY, "focus", m),
              this.event.bind(this.scrollbarY, "blur", E),
              (this.scrollbarYActive = null),
              (this.scrollbarYHeight = null),
              (this.scrollbarYTop = null),
              b().then(function () {
                var n = t(a.scrollbarXRail);
                ((a.scrollbarXBottom = parseInt(n.bottom, 10)),
                  isNaN(a.scrollbarXBottom)
                    ? ((a.isScrollbarXUsingBottom = !1), (a.scrollbarXTop = p(n.top)))
                    : (a.isScrollbarXUsingBottom = !0),
                  (a.railBorderXWidth = p(n.borderLeftWidth) + p(n.borderRightWidth)),
                  u(a.scrollbarXRail, { display: "block" }),
                  (a.railXMarginWidth = p(n.marginLeft) + p(n.marginRight)),
                  u(a.scrollbarXRail, { display: "" }),
                  (a.railXWidth = null),
                  (a.railXRatio = null));
                var r = t(a.scrollbarYRail);
                ((a.scrollbarYRight = parseInt(r.right, 10)),
                  isNaN(a.scrollbarYRight)
                    ? ((a.isScrollbarYUsingRight = !1), (a.scrollbarYLeft = p(r.left)))
                    : (a.isScrollbarYUsingRight = !0),
                  (a.scrollbarYOuterWidth = a.isRtl
                    ? (function (e) {
                        var u = t(e);
                        return (
                          p(u.width) +
                          p(u.paddingLeft) +
                          p(u.paddingRight) +
                          p(u.borderLeftWidth) +
                          p(u.borderRightWidth)
                        );
                      })(a.scrollbarY)
                    : null),
                  (a.railBorderYWidth = p(r.borderTopWidth) + p(r.borderBottomWidth)),
                  u(a.scrollbarYRail, { display: "block" }),
                  (a.railYMarginHeight = p(r.marginTop) + p(r.marginBottom)),
                  u(a.scrollbarXRail, { display: "" }),
                  u(a.scrollbarYRail, { display: "" }),
                  (a.railYHeight = null),
                  (a.railYRatio = null),
                  (a.reach = {
                    x:
                      e.scrollLeft <= 0
                        ? "start"
                        : e.scrollLeft >= a.contentWidth - a.containerWidth
                          ? "end"
                          : null,
                    y:
                      e.scrollTop <= 0
                        ? "start"
                        : e.scrollTop >= a.contentHeight - a.containerHeight
                          ? "end"
                          : null,
                  }),
                  (a.isAlive = !0),
                  a.settings.handlers.forEach(function (e) {
                    return N[e](a, a.settings.overScrollWidth);
                  }),
                  (a.boundHandleButtonEnter = a.handleMouseEnter.bind(a)),
                  (a.boundHandleMouseLeave = a.handleMouseLeave.bind(a)),
                  (a.boundHandleMouseEnter = a.handleMouseEnter.bind(a)),
                  (a.boundPlayClickSound = a.playClickSound.bind(a)),
                  a.scrollbarYButtonStart.addEventListener("mousedown", a.boundPlayClickSound),
                  a.scrollbarYButtonEnd.addEventListener("mousedown", a.boundPlayClickSound),
                  a.scrollbarXButtonStart.addEventListener("mousedown", a.boundPlayClickSound),
                  a.scrollbarXButtonEnd.addEventListener("mousedown", a.boundPlayClickSound),
                  a.scrollbarXButtonStart.addEventListener("mouseenter", a.boundHandleMouseEnter),
                  a.scrollbarXButtonEnd.addEventListener("mouseenter", a.boundHandleMouseEnter),
                  a.scrollbarYButtonStart.addEventListener("mouseenter", a.boundHandleButtonEnter),
                  a.scrollbarYButtonEnd.addEventListener("mouseenter", a.boundHandleButtonEnter),
                  a.scrollbarYButtonStart.addEventListener("mouseleave", a.boundHandleMouseLeave),
                  a.scrollbarYButtonEnd.addEventListener("mouseleave", a.boundHandleMouseLeave),
                  a.scrollbarY.addEventListener("mouseenter", a.boundHandleMouseEnter),
                  a.scrollbarX.addEventListener("mouseenter", a.boundHandleMouseEnter),
                  a.scrollbarY.addEventListener("mouseleave", a.boundHandleMouseLeave),
                  a.scrollbarY.addEventListener("mousedown", a.boundPlayClickSound),
                  a.scrollbarX.addEventListener("mousedown", a.boundPlayClickSound),
                  (a.lastScrollTop = Math.floor(e.scrollTop)),
                  (a.lastScrollLeft = e.scrollLeft),
                  (a.scrollTopPercent = e.scrollTop / e.scrollHeight),
                  (a.scrollLeftPercent = e.scrollLeft / e.scrollWidth),
                  a.event.bind(a.element, "scroll", function (e) {
                    return a.onScroll(e);
                  }),
                  a.settings.enableHorizontalScroll &&
                    a.event.bind(a.element, "wheel", function (e) {
                      return a.onWheel(e);
                    }),
                  C(a, !1, a.settings.overScrollWidth, !1));
              }));
          };
        ((R.prototype._getAnimationSettings = function (e, t, u, n) {
          var r = this,
            a = 0;
          return (
            null !== this.element &&
              (a = ["bottom", "top"].includes(t)
                ? this.element.scrollTop
                : this.element.scrollLeft),
            {
              scrollableDomEle: this.element,
              duration: this.settings.animationDuration,
              easingPreset: this.settings.animationEasingPreset,
              scrollAmount: e - a,
              direction: t,
              onRefUpdateCallback: function (e) {
                (C(r, !0, r.settings.overScrollWidth, !1), u && u(e));
              },
              onAnimationCompleteCallback: function () {
                n && n();
              },
            }
          );
        }),
          (R.prototype.playHoverSound = function () {
            window.engine && engine.call("PlaySound", "highlight");
          }),
          (R.prototype.playClickSound = function () {
            window.engine && engine.call("PlaySound", "play");
          }),
          (R.prototype.handleMouseEnter = function () {
            this.playHoverSound();
          }),
          (R.prototype.handleMouseLeave = function () {}),
          (R.prototype.update = function () {
            var e = this;
            this.isAlive &&
              ((this.negativeScrollAdjustment = this.isNegativeScroll
                ? this.element.scrollWidth - this.element.clientWidth
                : 0),
              u(this.scrollbarXRail, { display: "block" }),
              u(this.scrollbarYRail, { display: "block" }),
              (this.railXMarginWidth =
                p(t(this.scrollbarXRail).marginLeft) + p(t(this.scrollbarXRail).marginRight)),
              (this.railYMarginHeight =
                p(t(this.scrollbarYRail).marginTop) + p(t(this.scrollbarYRail).marginBottom)),
              u(this.scrollbarXRail, { display: "none" }),
              u(this.scrollbarYRail, { display: "none" }),
              b().then(function () {
                (e.settings.isDisableScrollToLastPositionOnResize ||
                  ((e.element.scrollTop = e.element.scrollHeight * e.scrollTopPercent),
                  (e.element.scrollLeft = e.element.scrollWidth * e.scrollLeftPercent)),
                  C(e, !1, e.settings.overScrollWidth, !1),
                  v(e, "top", 0, !1, !1, !0),
                  v(e, "left", 0, !1, !1, !0),
                  u(e.scrollbarXRail, { display: "" }),
                  u(e.scrollbarYRail, { display: "" }));
              }));
          }),
          (R.prototype.setScrollLeft = function (e, t, u) {
            S(this._getAnimationSettings(e, "right", t, u));
          }),
          (R.prototype.setScrollLeftImmediately = function (e) {
            ((this.element.scrollLeft = 0 | e), this.update());
          }),
          (R.prototype.setScrollTop = function (e, t, u) {
            S(this._getAnimationSettings(e, "bottom", t, u));
          }),
          (R.prototype.setScrollTopImmediately = function (e) {
            ((this.element.scrollTop = 0 | e), this.update());
          }),
          (R.prototype.onScroll = function (e) {
            this.isAlive && C(this, !1, this.settings.overScrollWidth, !0);
          }),
          (R.prototype.onWheel = function (e) {
            this.isAlive &&
              (C(this, !1, this.settings.overScrollWidth, !1),
              v(this, "left", this.element.scrollLeft - this.lastScrollLeft),
              (this.lastScrollLeft = this.element.scrollLeft));
          }),
          (R.prototype.destroy = function () {
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
              o(this.scrollbarX),
              o(this.scrollbarY),
              o(this.scrollbarXRail),
              o(this.scrollbarYRail),
              this.removePsClasses(),
              (this.element = null),
              (this.scrollbarX = null),
              (this.scrollbarY = null),
              (this.scrollbarXRail = null),
              (this.scrollbarYRail = null),
              (this.isAlive = !1));
          }),
          (R.prototype.removePsClasses = function () {
            this.element.className = this.element.className
              .split(" ")
              .filter(function (e) {
                return !e.match(/^ps([-_].+|)$/);
              })
              .join(" ");
          }),
          (e.exports = R));
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
      67: (e, t, u) => {
        "use strict";
        u.d(t, { O: () => K });
        var n = {};
        (u.r(n), u.d(n, { mouse: () => d, onResize: () => l }));
        var r = {};
        (u.r(r),
          u.d(r, {
            events: () => n,
            getMouseGlobalPosition: () => E,
            getSize: () => m,
            graphicsQuality: () => _,
          }));
        var a = {};
        (u.r(a), u.d(a, { getBgUrl: () => A, getTextureUrl: () => g }));
        var o = {};
        function i(e) {
          return (t) => (
            engine.on(e, t),
            () => {
              engine.off(e, t);
            }
          );
        }
        function s(e) {
          viewEnv.setTrackMouseOnStage(e);
        }
        (u.r(o),
          u.d(o, {
            addModelObserver: () => k,
            addPreloadTexture: () => w,
            children: () => a,
            displayStatus: () => h,
            displayStatusIs: () => $,
            events: () => p,
            extraSize: () => z,
            forceTriggerMouseMove: () => j,
            freezeTextureBeforeResize: () => R,
            getBrowserTexturePath: () => S,
            getDisplayStatus: () => G,
            getScale: () => M,
            getSize: () => L,
            getViewGlobalPosition: () => N,
            isClientAccessible: () => W,
            isEventHandled: () => Y,
            isFocused: () => H,
            pxToRem: () => O,
            remToPx: () => I,
            resize: () => T,
            sendEvent: () => B,
            setAnimateWindow: () => P,
            setEventHandled: () => X,
            setInputPaddingsRem: () => y,
            setSidePaddingsRem: () => x,
            whenTutorialReady: () => U,
          }));
        const l = i("clientResized"),
          c = { down: i("mousedown"), up: i("mouseup"), move: i("mousemove") };
        const d = (function () {
          const e = { listeners: 0, enabled: !0, initialized: !1 };
          function t() {
            e.enabled && s(!1);
          }
          function u() {
            e.enabled && s(!0);
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
              : s(!1);
          }
          const r = ["down", "up", "move"].reduce(
            (t, u) => (
              (t[u] = (function (t) {
                return (u) => {
                  e.listeners += 1;
                  let r = !0;
                  const a = `mouse${t}`,
                    o = c[t]((e) => u([e, "outside"]));
                  function i(e) {
                    u([e, "inside"]);
                  }
                  return (
                    window.addEventListener(a, i),
                    n(),
                    () => {
                      r &&
                        (o(), window.removeEventListener(a, i), (e.listeners -= 1), n(), (r = !1));
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
              e.enabled && s(!0);
            },
            disableOutside() {
              e.enabled && s(!1);
            },
          });
        })();
        function m(e = "px") {
          return "rem" === e ? viewEnv.getClientSizeRem() : viewEnv.getClientSizePx();
        }
        function E(e = "px") {
          return "rem" === e
            ? viewEnv.getMouseGlobalPositionRem()
            : viewEnv.getMouseGlobalPositionPx();
        }
        const _ = {
          isLow: () => 1 === viewEnv.getGraphicsQuality(),
          isHigh: () => 0 === viewEnv.getGraphicsQuality(),
          get: () => viewEnv.getGraphicsQuality(),
        };
        function g(e, t, u = 1) {
          return viewEnv.getChildTexturePath(e, t.width, t.height, u);
        }
        function A(e, t, u) {
          return `url(${g(e, t, u)})`;
        }
        const h = { showing: 0, shown: 1, hiding: 2, hidden: 3 },
          p = {
            onTextureFrozen: i("self.onTextureFrozen"),
            onTextureReady: i("self.onTextureReady"),
            onDomBuilt: i("self.onDomBuilt"),
            onLoaded: i("self.onLoaded"),
            onDisplayChanged: i("self.onShowingStatusChanged"),
            onFocusUpdated: i("self.onFocusChanged"),
            children: {
              onAdded: i("children.onAdded"),
              onLoaded: i("children.onLoaded"),
              onRemoved: i("children.onRemoved"),
              onAttached: i("children.onAttached"),
              onTextureReady: i("children.onTextureReady"),
              onRequestPosition: i("children.requestPosition"),
            },
          },
          F = ["args"];
        const b = 2,
          D = 16,
          v = 32,
          C = 64,
          f = (e, t) => {
            const u = "GFViewEventProxy";
            if (void 0 !== t) {
              const r = t.args,
                a = (function (e, t) {
                  if (null == e) return {};
                  var u,
                    n,
                    r = {},
                    a = Object.keys(e);
                  for (n = 0; n < a.length; n++) ((u = a[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
                  return r;
                })(t, F);
              return void 0 !== r
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: u, type: e }, a, {
                      arguments:
                        ((n = r),
                        Object.entries(n).map(([e, t]) => {
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
            var n;
          },
          B = {
            close(e) {
              f("popover" === e ? b : v);
            },
            minimize() {
              f(C);
            },
            move(e) {
              f(D, { isMouseEvent: !0, on: e });
            },
          };
        function w(e) {
          viewEnv.addPreloadTexture(e);
        }
        function y(e) {
          viewEnv.setHitAreaPaddingsRem(e, e, e, e, 15);
        }
        function S(e, t, u, n = 1) {
          return viewEnv.getWebBrowserTexturePath(e, t, u, n);
        }
        function k(e, t, u) {
          return viewEnv.addDataChangedCallback(e, t, u);
        }
        function x(e) {
          viewEnv.setHitAreaPaddingsRem(e.top, e.right, e.bottom, e.left, 15);
        }
        function L(e = "px") {
          return "rem" === e ? viewEnv.getViewSizeRem() : viewEnv.getViewSizePx();
        }
        function T(e, t, u = "px") {
          return "rem" === u ? viewEnv.resizeViewRem(e, t) : viewEnv.resizeViewPx(e, t);
        }
        function N(e = "rem") {
          const t = viewEnv.getViewGlobalPositionRem();
          return "rem" === e ? t : { x: I(t.x), y: I(t.y) };
        }
        function R() {
          viewEnv.freezeTextureBeforeResize();
        }
        function M() {
          return viewEnv.getScale();
        }
        function O(e) {
          return viewEnv.pxToRem(e);
        }
        function I(e) {
          return viewEnv.remToPx(e);
        }
        function P(e, t) {
          viewEnv.setAnimateWindow(e, t);
        }
        function H() {
          return viewEnv.isFocused();
        }
        function W() {
          return viewEnv.isClientAccessible();
        }
        function X() {
          return viewEnv.setEventHandled();
        }
        function Y() {
          return viewEnv.isEventHandled();
        }
        function j() {
          viewEnv.forceTriggerMouseMove();
        }
        function G() {
          return viewEnv.getShowingStatus();
        }
        const $ = Object.keys(h).reduce(
            (e, t) => ((e[t] = () => viewEnv.getShowingStatus() === h[t]), e),
            {},
          ),
          z = {
            set: (e, t) => {
              viewEnv.setExtraSizeRem(e, t);
            },
            get: (e, t) => {
              viewEnv.getExtraSizeRem(e, t);
            },
          },
          U = Promise.all([
            new Promise((e) => {
              window.isDomBuilt ? e() : p.onDomBuilt(e);
            }),
            engine.whenReady,
          ]),
          K = { view: o, client: r };
      },
      358: (e, t, u) => {
        "use strict";
        u.d(t, { Z: () => a });
        var n = u(67);
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
            const a = n.O.view.addModelObserver(e, u, r);
            return (
              a > 0
                ? ((this._callbacks[a] = t),
                  u > 0 && (this._views[u] ? this._views[u].push(a) : (this._views[u] = [a])))
                : console.error("Can't add callback for model:", e),
              a
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
        const a = r;
      },
      572: (__unused_webpack_module, __webpack_exports__, __webpack_require__) => {
        "use strict";
        __webpack_require__.d(__webpack_exports__, { Z: () => __WEBPACK_DEFAULT_EXPORT__ });
        var _DataTracker__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(358),
          _index__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(596);
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
      596: (e, t, u) => {
        "use strict";
        u.d(t, { Sw: () => a.Z, Gr: () => d, Z5: () => i, B0: () => l, lw: () => o, ry: () => b });
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
        var a = u(358);
        function o(e) {
          const t = {};
          if ("object" != typeof e) return e;
          for (const u in e)
            if (Object.prototype.hasOwnProperty.call(e, u)) {
              const n = Object.prototype.toString.call(e[u]);
              if (n.startsWith("[object CoherentArrayProxy]")) {
                const n = e[u];
                t[u] = [];
                for (let e = 0; e < n.length; e++) t[u].push({ value: o(n[e].value) });
              } else
                n.startsWith("[object class BW::WULF::ViewModel")
                  ? (t[u] = o(e[u]))
                  : (t[u] = e[u]);
            }
          return t;
        }
        const i = {
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
        const c = Object.freeze({ INTEGRAL: 0, GOLD: 1 }),
          d = Object.freeze({ FRACTIONAL: 0, WO_ZERO_DIGITS: 1 }),
          m = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1 }),
          E = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1, YEAR_MONTH: 2 });
        let _, g;
        (!(function (e) {
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
        })(_ || (_ = {})),
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
          })(g || (g = {})));
        var A = u(67);
        const h = ["args"];
        function p(e, t, u, n, r, a, o) {
          try {
            var i = e[a](o),
              s = i.value;
          } catch (e) {
            return void u(e);
          }
          i.done ? t(s) : Promise.resolve(s).then(n, r);
        }
        const F = (e) => ({
            __Type: "GFBoundingBox",
            x: e.x,
            y: e.y,
            width: e.width,
            height: e.height,
          }),
          b = (function () {
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
                    var a = e.apply(t, u);
                    function o(e) {
                      p(a, n, r, o, i, "next", e);
                    }
                    function i(e) {
                      p(a, n, r, o, i, "throw", e);
                    }
                    o(void 0);
                  });
                });
            return function () {
              return t.apply(this, arguments);
            };
          })(),
          D = (e, t) => {
            const u = "GFViewEventProxy";
            if (void 0 !== t) {
              const r = t.args,
                a = (function (e, t) {
                  if (null == e) return {};
                  var u,
                    n,
                    r = {},
                    a = Object.keys(e);
                  for (n = 0; n < a.length; n++) ((u = a[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
                  return r;
                })(t, h);
              void 0 !== r
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: u, type: e }, a, {
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
                : viewEnv.handleViewEvent(Object.assign({ __Type: u, type: e }, a));
            } else viewEnv.handleViewEvent({ __Type: u, type: e });
            var n;
          },
          v = () => D(l.CLOSE),
          C = (e, t) => {
            e.keyCode === _.ESCAPE && t();
          };
        var f = u(572);
        const B = r.instance,
          w = {
            DataTracker: a.Z,
            ViewModel: f.Z,
            ViewEventType: l,
            NumberFormatType: c,
            RealFormatType: d,
            TimeFormatType: m,
            DateFormatType: E,
            makeGlobalBoundingBox: F,
            sendMoveEvent: (e) => D(l.MOVE, { isMouseEvent: !0, on: e }),
            sendCloseEvent: v,
            sendClosePopOverEvent: () => D(l.POP_OVER, { on: !1 }),
            sendShowContextMenuEvent: (e, t, u = 0) => {
              D(l.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: e,
                on: !0,
                decoratorID: u,
                args: t,
              });
            },
            sendShowPopOverEvent: (e, t, u, n, r = R.invalid("resId"), a) => {
              const o = A.O.view.getViewGlobalPosition(),
                i = u.getBoundingClientRect(),
                s = i.x,
                c = i.y,
                d = i.width,
                m = i.height,
                E = {
                  x: A.O.view.pxToRem(s) + o.x,
                  y: A.O.view.pxToRem(c) + o.y,
                  width: A.O.view.pxToRem(d),
                  height: A.O.view.pxToRem(m),
                };
              D(l.POP_OVER, {
                isMouseEvent: !0,
                contentID: e,
                decoratorID: n || R.invalid("resId"),
                targetID: r,
                direction: t,
                bbox: F(E),
                on: !0,
                args: a,
              });
            },
            addEscapeListener: (e) => {
              const t = (t) => C(t, e);
              return (
                window.addEventListener("keydown", t),
                () => window.removeEventListener("keydown", t)
              );
            },
            closeOnEsc: (e) => {
              C(e, v);
            },
            handleViewEvent: D,
            onBindingsReady: b,
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
            dumpViewModel: o,
            ClickOutsideManager: B,
            SystemLocale: i,
            UserLocale: s,
          };
        window.ViewEnvHelper = w;
      },
      978: (e, t, u) => {
        "use strict";
        var n = u(483),
          r = u.n(n);
        function a(e) {
          engine.call("PlaySound", e);
        }
        var o = u(179),
          i = u.n(o);
        const s = {
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
        let l, c;
        (!(function (e) {
          ((e.main = "main"),
            (e.primary = "primary"),
            (e.primaryGreen = "primaryGreen"),
            (e.primaryRed = "primaryRed"),
            (e.secondary = "secondary"),
            (e.ghost = "ghost"));
        })(l || (l = {})),
          (function (e) {
            ((e.extraSmall = "extraSmall"), (e.small = "small"), (e.medium = "medium"));
          })(c || (c = {})));
        const d = ({
          children: e,
          size: t,
          isFocused: u,
          type: n,
          disabled: c,
          mixClass: d,
          soundHover: m,
          soundClick: E,
          onMouseEnter: _,
          onMouseMove: g,
          onMouseDown: A,
          onMouseUp: h,
          onMouseLeave: p,
          onClick: F,
        }) => {
          const b = (0, o.useRef)(null),
            D = (0, o.useState)(u),
            v = D[0],
            C = D[1],
            f = (0, o.useState)(!1),
            B = f[0],
            w = f[1],
            y = (0, o.useState)(!1),
            S = y[0],
            k = y[1],
            x = (0, o.useCallback)(() => {
              c || (b.current && (b.current.focus(), C(!0)));
            }, [c]),
            L = (0, o.useCallback)(
              (e) => {
                v && null !== b.current && !b.current.contains(e.target) && C(!1);
              },
              [v],
            ),
            T = (0, o.useCallback)(
              (e) => {
                c || (F && F(e));
              },
              [c, F],
            ),
            N = (0, o.useCallback)(
              (e) => {
                c || (null !== m && a(m), _ && _(e), k(!0));
              },
              [c, m, _],
            ),
            M = (0, o.useCallback)(
              (e) => {
                g && g(e);
              },
              [g],
            ),
            O = (0, o.useCallback)(
              (e) => {
                c || (h && h(e), w(!1));
              },
              [c, h],
            ),
            I = (0, o.useCallback)(
              (e) => {
                c || (null !== E && a(E), A && A(e), u && x(), w(!0));
              },
              [c, E, A, x, u],
            ),
            P = (0, o.useCallback)(
              (e) => {
                c || (p && p(e), w(!1));
              },
              [c, p],
            ),
            H = r()(
              s.base,
              s[`base__${n}`],
              {
                [s.base__disabled]: c,
                [s[`base__${t}`]]: t,
                [s.base__focus]: v,
                [s.base__highlightActive]: B,
                [s.base__firstHover]: S,
              },
              d,
            ),
            W = r()(s.state, s.state__default);
          return (
            (0, o.useEffect)(
              () => (
                document.addEventListener("mousedown", L),
                () => {
                  document.removeEventListener("mousedown", L);
                }
              ),
              [L],
            ),
            (0, o.useEffect)(() => {
              C(u);
            }, [u]),
            i().createElement(
              "div",
              {
                ref: b,
                className: H,
                onMouseEnter: N,
                onMouseMove: M,
                onMouseUp: O,
                onMouseDown: I,
                onMouseLeave: P,
                onClick: T,
              },
              n !== l.ghost &&
                i().createElement(
                  i().Fragment,
                  null,
                  i().createElement("div", { className: s.back }),
                  i().createElement("span", { className: s.texture }),
                ),
              i().createElement(
                "span",
                { className: W },
                i().createElement("span", { className: s.stateDisabled }),
                i().createElement("span", { className: s.stateHighlightHover }),
                i().createElement("span", { className: s.stateHighlightActive }),
              ),
              i().createElement(
                "span",
                { className: s.content, lang: R.strings.settings.LANGUAGE_CODE() },
                e,
              ),
            )
          );
        };
        d.defaultProps = {
          type: l.primary,
          isFocused: !1,
          soundHover: "highlight",
          soundClick: "play",
        };
        const m = (0, o.memo)(d),
          E = {
            base: "ErrorBoundary_base_46",
            message: "ErrorBoundary_message_33",
            heading: "ErrorBoundary_heading_ba",
            button: "ErrorBoundary_button_74",
            errorStack: "ErrorBoundary_errorStack_fe",
            errorInfo: "ErrorBoundary_errorInfo_f1",
          };
        class _ extends i().Component {
          constructor(e) {
            (super(e),
              (this.clearError = () => {
                this.setState({ error: void 0 });
              }),
              (this.state = { error: void 0 }));
          }
          static getDerivedStateFromError(e) {
            return { error: e };
          }
          render() {
            const e = this.state.error,
              t = this.props,
              u = t.errorMessage,
              n = void 0 === u ? R.strings.dogtags.error.message() : u,
              r = t.retryLabel,
              a = void 0 === r ? R.strings.dogtags.error.retry() : r;
            return e
              ? i().createElement(
                  "div",
                  { className: E.base },
                  i().createElement(
                    "div",
                    { className: E.message },
                    i().createElement("div", { className: E.heading }, n),
                    i().createElement(m, { mixClass: E.retry, onClick: this.clearError }, a),
                  ),
                )
              : this.props.children;
          }
        }
        var g = u(493),
          A = u.n(g);
        const h = {
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
          p = [
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
        function F() {
          return (
            (F =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            F.apply(this, arguments)
          );
        }
        class b extends i().PureComponent {
          constructor(...e) {
            (super(...e),
              (this.state = { hover: !1, click: !1 }),
              (this._onMouseEnter = (e) => (t) => {
                (e && e(t),
                  this.setState({ hover: !0 }),
                  this.props.soundHover && a(this.props.soundHover));
              }),
              (this._onMouseLeave = (e) => (t) => {
                (e && e(t), this.setState({ hover: !1, click: !1 }));
              }),
              (this._onMouseDown = (e) => (t) => {
                (e && e(t),
                  this.setState({ click: !0 }),
                  this.props.soundClick && a(this.props.soundClick));
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
              o = e.type,
              s = e.classNames,
              l = e.onMouseEnter,
              c = e.onMouseLeave,
              d = e.onMouseDown,
              m = e.onMouseUp,
              E =
                (e.soundClick,
                e.soundHover,
                (function (e, t) {
                  if (null == e) return {};
                  var u,
                    n,
                    r = {},
                    a = Object.keys(e);
                  for (n = 0; n < a.length; n++) ((u = a[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
                  return r;
                })(e, p)),
              _ = r()(h.base, h[`base__${o}`], h[`base__${a}`], null == s ? void 0 : s.base),
              g = r()(h.icon, h[`icon__${o}`], h[`icon__${a}`], null == s ? void 0 : s.icon),
              A = r()(h.glow, null == s ? void 0 : s.glow),
              b = r()(h.caption, h[`caption__${o}`], null == s ? void 0 : s.caption),
              D = r()(h.goto, null == s ? void 0 : s.goto);
            return i().createElement(
              "div",
              F(
                {
                  className: _,
                  onMouseEnter: this._onMouseEnter(l),
                  onMouseLeave: this._onMouseLeave(c),
                  onMouseDown: this._onMouseDown(d),
                  onMouseUp: this._onMouseUp(m),
                  onFocus: this.handleFocus,
                  onBlur: this.handleBlur,
                  onClick: u,
                },
                E,
              ),
              "info" !== o && i().createElement("div", { className: h.shine }),
              i().createElement(
                "div",
                { className: g },
                i().createElement("div", { className: A }),
              ),
              i().createElement("div", { className: b }, t),
              n && i().createElement("div", { className: D }, n),
            );
          }
        }
        b.defaultProps = {
          side: "left",
          type: "back",
          soundHover: "highlight",
          soundClick: "play",
        };
        const D = (e, t) => {
            let u;
            const n = setTimeout(() => {
              u = e();
            }, t);
            return () => {
              ("function" == typeof u && u(), clearTimeout(n));
            };
          },
          v = (e = 1) => {
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
          },
          C = (e, t) => e.split(".").reduce((e, t) => e && e[t], t),
          f = (e) => {
            const t = (0, o.useRef)(!1);
            t.current || (e(), (t.current = !0));
          };
        var B = u(596);
        const w = (e) => e && "ArrayItem" === e.__proto__.constructor.name,
          y = (e, t) => (e.length > 0 ? `${e}.${t}` : t),
          S = (e) =>
            ((e, t) =>
              e.split(".").reduce((e, u) => {
                const n = C(`${e}.${u}`, window);
                return w(n) ? t(e, u, n) : `${e}.${u}`;
              }))(e, (e, t) => `${e}.${t}.value`),
          k = (e) => {
            const t = ((e) => {
                const t = v(),
                  u = t.caller,
                  n = t.resId,
                  r = window.__feature && window.__feature !== u && u ? `subViews.${u}` : "";
                return { modelPrefix: r, modelPath: y(r, e || ""), resId: n };
              })(),
              u = t.modelPrefix,
              n = e.split(".");
            if (n.length > 0) {
              const e = [n[0]];
              return (
                n.reduce((t, n) => {
                  const r = C(y(u, `${t}.${n}`), window);
                  return w(r) ? (e.push(r.id), `${t}.${n}.value`) : (e.push(n), `${t}.${n}`);
                }),
                e.reduce((e, t) => e + "." + t)
              );
            }
            return "";
          },
          x = B.Sw.instance;
        let L;
        !(function (e) {
          ((e.None = "None"), (e.Shallow = "Shallow"), (e.Deep = "Deep"));
        })(L || (L = {}));
        const T = (e = "model", t = L.Deep) => {
          const u = (0, o.useState)(0),
            n = (u[0], u[1]),
            r = (0, o.useMemo)(() => v(), []),
            a = r.caller,
            i = r.resId,
            s = (0, o.useMemo)(
              () => (window.__feature && window.__feature !== a ? `subViews.${a}.${e}` : e),
              [a, e],
            ),
            l = (0, o.useState)(() =>
              ((e) => {
                const t = C(e, window);
                for (const e in t) "function" == typeof t[e] && (t[e] = t[e].bind(t));
                return w(t) ? t.value : t;
              })(S(s)),
            ),
            c = l[0],
            d = l[1],
            m = (0, o.useRef)(-1);
          return (
            f(() => {
              if (
                ("boolean" == typeof t &&
                  ((t = t ? L.Deep : L.None),
                  console.warn(
                    'Boolean key for useModel "tracking" param is deprecated. Use ModelTracking enum values instead!',
                  )),
                t !== L.None)
              ) {
                const u = (e) => {
                    ((e) => e && "CoherentArrayProxy" === e.__proto__.constructor.name)(e) &&
                    t === L.Deep
                      ? (e === c && n((e) => e + 1), d(e))
                      : d(Object.assign([], e));
                  },
                  r = k(e);
                m.current = x.addCallback(r, u, i, t === L.Deep);
              }
            }),
            (0, o.useEffect)(() => {
              if (t !== L.None)
                return () => {
                  x.removeCallback(m.current, i);
                };
            }, [i, t]),
            c
          );
        };
        let N, M, O, I, P;
        (!(function (e) {
          ((e[(e.Engraving = 0)] = "Engraving"), (e[(e.Background = 1)] = "Background"));
        })(N || (N = {})),
          (function (e) {
            ((e[(e.Equipped = 0)] = "Equipped"),
              (e[(e.Locked = 1)] = "Locked"),
              (e[(e.Open = 2)] = "Open"));
          })(M || (M = {})),
          (function (e) {
            ((e.Engraving = "engraving"), (e.Background = "background"));
          })(O || (O = {})),
          (function (e) {
            ((e.Dedication = "dedication"),
              (e.Skill = "skill"),
              (e.RankedSkill = "ranked_skill"),
              (e.Triumph = "triumph"),
              (e.Medal = "triumph_medal"),
              (e.Base = "base"),
              (e.Static = "static"));
          })(I || (I = {})),
          (function (e) {
            ((e.Dedication = "dedication"),
              (e.Triumph = "triumph"),
              (e.Season = "season"),
              (e.Static = "static"));
          })(P || (P = {})));
        const H = {
            [P.Dedication]: [I.Dedication],
            [P.Triumph]: [I.Triumph],
            [P.Season]: [I.Skill, I.RankedSkill],
            [P.Static]: [I.Static],
          },
          W = 10;
        let X;
        function Y(e, t) {
          var u = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (u) return (u = u.call(e)).next.bind(u);
          if (
            Array.isArray(e) ||
            (u = (function (e, t) {
              if (!e) return;
              if ("string" == typeof e) return j(e, t);
              var u = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === u && e.constructor && (u = e.constructor.name);
              if ("Map" === u || "Set" === u) return Array.from(e);
              if ("Arguments" === u || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(u))
                return j(e, t);
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
        function j(e, t) {
          (null == t || t > e.length) && (t = e.length);
          for (var u = 0, n = new Array(t); u < t; u++) n[u] = e[u];
          return n;
        }
        !(function (e) {
          ((e.NUMBER = "NUMBER"), (e.PERCENTAGE = "PERCENTAGE"));
        })(X || (X = {}));
        const G = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"],
          $ = (e, t) => {
            const u = e.id;
            return u === t.background.id || u === t.engraving.id;
          },
          z = R.images.gui.maps.icons.dogtags,
          U = "R.images.gui.maps.icons.dogtags",
          K = R.strings.dogtags.component,
          V = "R.strings.dogtags.component",
          q = (e, t, u, n = 0, r = "big", a = z, o = K) => {
            a &&
              !(r in a) &&
              console.error(
                `componentResourcesMap error at id: ${e}. Property "${r}" does not exist in ${U}`,
              );
            const i = r in a ? a[r] : void 0,
              s = `${t}s`;
            i &&
              !(s in i) &&
              console.error(
                `componentResourcesMap error at id: ${e}. Property "${s}" does not exist in ${[U, r].join(".")}`,
              );
            const l = i && s in i ? i[s] : void 0,
              c = `${t}_${e}_${t === O.Engraving ? n : "0"}`;
            l &&
              !(c in l) &&
              console.error(
                `componentResourcesMap error at id: ${e}. Property "${c}" does not exist in ${[U, r, s].join(".")}`,
              );
            const d = l && c in l ? l[c]() : a.big.backgrounds.background_66_0();
            o &&
              !(t in o) &&
              console.error(
                `componentResourcesMap error at id: ${e}. Property "${t}" does not exist in ${V}`,
              );
            const m = t in o ? o[t] : void 0;
            m &&
              !(u in m) &&
              console.error(
                `componentResourcesMap error at id: ${e}. Property "${u}" does not exist in ${[V, t].join(".")}`,
              );
            const E = m && u in m ? m[u] : void 0,
              _ = `c_${e}`;
            E &&
              !(_ in E) &&
              console.error(
                `componentResourcesMap error at id: ${e}. Property "${_}" does not exist in ${[V, t, u].join(".")}`,
              );
            return { image: d, strings: E && _ in E ? E[_] : void 0 };
          },
          Z = (e) => e.filter((e) => e.value.items.length > 0),
          Q = (e) => Object.keys(e).filter((t) => e[t]),
          J = { [N.Engraving]: "engravingGrid", [N.Background]: "backgroundGrid" },
          ee = { [N.Engraving]: "engraving", [N.Background]: "background" },
          te = (e, t) => {
            for (var u, n = Y(e.values()); !(u = n()).done;) {
              for (var r, a = Y(u.value.value.items.values()); !(r = a()).done;) {
                const e = r.value;
                if (e.value.id === t) return e.value;
              }
            }
          },
          ue = (e) => e.reduce((e, t) => e + t.value.items.length, 0),
          ne = (e, t = X.NUMBER) => {
            const u = B.Z5.getRealFormat(e, B.Gr.WO_ZERO_DIGITS).replace(/\s/g, " ");
            return t === X.PERCENTAGE ? `${u} %` : u;
          },
          re = {
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
          ae = [
            "size",
            "value",
            "isEmpty",
            "fadeInAnimation",
            "hide",
            "maximumNumber",
            "className",
          ];
        function oe() {
          return (
            (oe =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            oe.apply(this, arguments)
          );
        }
        const ie = (e) => {
          let t = e.size,
            u = e.value,
            n = e.isEmpty,
            a = e.fadeInAnimation,
            o = e.hide,
            s = e.maximumNumber,
            l = e.className,
            c = (function (e, t) {
              if (null == e) return {};
              var u,
                n,
                r = {},
                a = Object.keys(e);
              for (n = 0; n < a.length; n++) ((u = a[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
              return r;
            })(e, ae);
          const d = n ? null : u,
            m = "string" == typeof d;
          if ((d && !m && d < 0) || 0 === d) return null;
          const E = d && !m && d > s,
            _ = r()(
              re.base,
              re[`base__${t}`],
              a && re.base__animated,
              o && re.base__hidden,
              !d && re.base__pattern,
              n && re.base__empty,
              l,
            );
          return i().createElement(
            "div",
            oe({ className: _ }, c),
            i().createElement("div", { className: re.bg }),
            i().createElement("div", { className: re.pattern }),
            i().createElement(
              "div",
              { className: r()(re.value, m && re.value__text) },
              E ? s : d,
              E && i().createElement("span", { className: re.plus }, "+"),
            ),
          );
        };
        ie.defaultProps = { size: "normal", fadeInAnimation: !1, hide: !1, maximumNumber: 99 };
        const se = R.images.gui.maps.icons.dogtags.big.digits,
          le = (e, t = se) => {
            const u = `c_${e}`;
            return u in t
              ? t[u]()
              : e in t
                ? t[e]()
                : void (
                    "invalidTestDigit" !== e &&
                    console.error(
                      `getDigitUri error at digit: ${e}. No properties "${u}" nor "${e}" exist in R.images.gui.maps.icons.dogtags.big.digits`,
                    )
                  );
          },
          ce = (e) => ({ backgroundImage: `url(${e})` }),
          de = "Item_base_13",
          me = "Item_mainWrapper_0c",
          Ee = "Item_hoverWrapper_2e",
          _e = "Item_base__selected_f0",
          ge = "Item_slotBg_3d",
          Ae = "Item_selectedBg_7c",
          he = "Item_hoverBg_8d",
          pe = "Item_hoverInfo_05",
          Fe = "Item_base__locked_59",
          be = "Item_componentImage_03",
          De = "Item_engravingBackground_e6",
          ve = "Item_statusIcon_69",
          Ce = "Item_statusIcon_check_0c",
          fe = "Item_statusIcon_lock_5b",
          Be = "Item_levelBadge_13",
          we = "Item_itemCounter_cb",
          ye = ["selected", "isEquipped", "onNewComponentHover"];
        const Se = R.images.gui.maps.icons.dogtags,
          ke = r()(be, De),
          xe = (0, o.memo)((e) => {
            const t = e.selected,
              u = e.isEquipped,
              n = e.onNewComponentHover,
              s = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  r = {},
                  a = Object.keys(e);
                for (n = 0; n < a.length; n++) ((u = a[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
                return r;
              })(e, ye),
              l = s.id,
              c = s.type,
              d = s.isLocked,
              m = s.currentGrade,
              E = s.currentProgress,
              _ = s.progressNumberType,
              g = s.onClick,
              A = s.purpose,
              h = s.isNew;
            let p = null;
            d
              ? (p = t ? Se.icons.alert() : Se.icons.lock())
              : u && (p = Se.icons.equipped_slot_icon());
            const F = p ? ce(p) : {},
              b = m,
              D = q(l, c, A, b, "small"),
              v = D.image,
              C = D.strings,
              f = c === O.Engraving,
              B = (0, o.useCallback)(() => {
                (a(d ? R.sounds.dt_element_locked_click() : R.sounds.dt_element_click()), g(s));
              }, [d, g, s]),
              w = (0, o.useCallback)(() => {
                h && n({ compId: l });
              }, [l, n, h]),
              y = (0, o.useCallback)(() => {
                a(R.sounds.highlight());
              }, []);
            if (!C) return (console.warn(`Component ${l} is missing translation info.`), null);
            const S = C.title(),
              k = ce(v),
              x = r()(de, { [_e]: t, [Fe]: d }),
              L = ne(E, _),
              T = r()(ve, { [Ce]: u && !d, [fe]: !t && d }),
              N = A === I.Static,
              M = !d && f,
              P = i().createElement("div", { className: be, style: k });
            return i().createElement(
              "div",
              { className: x, onClick: B, onMouseOver: w, onMouseEnter: y, id: "item-" + l },
              i().createElement(
                "div",
                { className: me },
                i().createElement("div", { className: ge }),
                i().createElement("div", { className: Ae }),
                b >= 0 && M && !N && i().createElement("div", { className: Be }, G[b]),
                f ? i().createElement("div", { className: ke }, P) : P,
                p && i().createElement("div", { className: T, style: F }),
                i().createElement(
                  "div",
                  { className: Ee },
                  i().createElement("div", { className: he }),
                  i().createElement(
                    "div",
                    { className: pe },
                    S,
                    M && i().createElement("span", null, L),
                  ),
                ),
              ),
              h &&
                i().createElement("div", { className: we }, i().createElement(ie, { isEmpty: !0 })),
            );
          }),
          Le = [
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
        function Te(e) {
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
        const Ne = (e, t, u = {}, n = 0) => {
            viewEnv.handleViewEvent(
              Object.assign(
                {
                  __Type: "GFViewEventProxy",
                  type: B.B0.TOOLTIP,
                  contentID: e,
                  decoratorID: t,
                  targetID: n,
                },
                u,
              ),
            );
          },
          Re = (e) => {
            let t = e.children,
              u = e.contentId,
              n = e.args,
              r = e.onMouseEnter,
              a = e.onMouseLeave,
              i = e.onMouseDown,
              s = e.onClick,
              l = e.ignoreShowDelay,
              c = void 0 !== l && l,
              d = e.ignoreMouseClick,
              m = void 0 !== d && d,
              E = e.decoratorId,
              _ = void 0 === E ? 0 : E,
              g = e.isEnabled,
              A = void 0 === g || g,
              h = e.targetId,
              p = void 0 === h ? 0 : h,
              F = e.onShow,
              b = e.onHide,
              D = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  r = {},
                  a = Object.keys(e);
                for (n = 0; n < a.length; n++) ((u = a[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
                return r;
              })(e, Le);
            const C = (0, o.useRef)({
                timeoutId: 0,
                isVisible: !1,
                prevTarget: null,
                hideTimerId: null,
              }),
              f = (0, o.useMemo)(() => p || v().resId, [p]),
              B = (0, o.useCallback)(() => {
                (C.current.isVisible && C.current.timeoutId) ||
                  (Ne(u, _, { isMouseEvent: !0, on: !0, arguments: Te(n) }, f),
                  F && F(),
                  (C.current.isVisible = !0));
              }, [u, _, n, f, F]),
              w = (0, o.useCallback)(() => {
                if (C.current.isVisible || C.current.timeoutId) {
                  const e = C.current.timeoutId;
                  (e > 0 && (clearTimeout(e), (C.current.timeoutId = 0)),
                    Ne(u, _, { on: !1 }, f),
                    C.current.isVisible && b && b(),
                    (C.current.isVisible = !1));
                }
              }, [u, _, f, b]),
              y = (0, o.useCallback)((e) => {
                C.current.isVisible &&
                  ((C.current.prevTarget = document.elementFromPoint(e.clientX, e.clientY)),
                  (C.current.hideTimerId = window.setTimeout(() => {
                    const t = document.elementFromPoint(e.clientX, e.clientY);
                    t && !t.isSameNode(C.current.prevTarget) && w();
                  }, 200)));
              }, []);
            ((0, o.useEffect)(() => {
              const e = C.current.hideTimerId;
              return (
                document.addEventListener("wheel", y, { capture: !0 }),
                () => {
                  (document.removeEventListener("wheel", y, { capture: !0 }),
                    e && window.clearTimeout(e));
                }
              );
            }, []),
              (0, o.useEffect)(() => {
                !1 === A && w();
              }, [A, w]),
              (0, o.useEffect)(
                () => (
                  window.addEventListener("mouseleave", w),
                  () => {
                    (window.removeEventListener("mouseleave", w), w());
                  }
                ),
                [w],
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
                            ((C.current.timeoutId = window.setTimeout(B, c ? 100 : 400)),
                            r && r(e),
                            S && S(e));
                        }),
                      onMouseLeave: ((e) => (t) => {
                        (w(), null == a || a(t), null == e || e(t));
                      })(t.props.onMouseLeave),
                      onClick: ((e) => (t) => {
                        (!1 === m && w(), null == s || s(t), null == e || e(t));
                      })(t.props.onClick),
                      onMouseDown: ((e) => (t) => {
                        (!1 === m && w(), null == i || i(t), null == e || e(t));
                      })(t.props.onMouseDown),
                    },
                    D,
                  ),
                )
              : t;
            var S;
          },
          Me = ["children", "body", "header", "note", "alert", "args"];
        function Oe() {
          return (
            (Oe =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            Oe.apply(this, arguments)
          );
        }
        const Ie = R.views.common.tooltip_window.simple_tooltip_content,
          Pe = (e) => {
            let t = e.children,
              u = e.body,
              n = e.header,
              r = e.note,
              a = e.alert,
              s = e.args,
              l = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  r = {},
                  a = Object.keys(e);
                for (n = 0; n < a.length; n++) ((u = a[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
                return r;
              })(e, Me);
            const c = (0, o.useMemo)(() => {
              const e = Object.assign({}, s, { body: u, header: n, note: r, alert: a });
              for (const t in e) void 0 === e[t] && delete e[t];
              return e;
            }, [a, u, n, r, s]);
            return i().createElement(
              Re,
              Oe(
                {
                  contentId:
                    ((d = null == s ? void 0 : s.hasHtmlContent),
                    d ? Ie.SimpleTooltipHtmlContent("resId") : Ie.SimpleTooltipContent("resId")),
                  decoratorId: R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
                  args: c,
                },
                l,
              ),
              t,
            );
            var d;
          },
          He = "Grid_base_2f",
          We = "Grid_sectionWrapper_fa",
          Xe = "Grid_emptyBlock_30",
          Ye = "Grid_sectionTitle_79",
          je = "Grid_sectionTitle_text_63",
          Ge = "Grid_sectionTitle_unlockedCount_fb",
          $e = "Grid_sectionTitle_count_ac",
          ze = "Grid_sectionTitle_infoIcon_d7";
        function Ue() {
          return (
            (Ue =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            Ue.apply(this, arguments)
          );
        }
        const Ke = (0, o.memo)(
            ({
              data: e,
              onItemSelect: t,
              onNewComponentHover: u,
              selectedItems: n,
              equippedItems: r,
            }) =>
              i().createElement(
                "div",
                { className: He },
                e.map((e, a) => {
                  const o = e.value.items.length,
                    s = (3 - (o % 3)) % 3,
                    l = Array.from(Array(s)).map((e, t) =>
                      i().createElement("div", { key: "emptyBlock-" + t, className: Xe }),
                    ),
                    c = e.value.items.reduce((e, t) => (t.value.isLocked ? e : e + 1), 0),
                    d = e.value.title ? systemLocale.toUpperCase(e.value.title) : "";
                  return i().createElement(
                    "div",
                    { key: `${e.value.title}-${a}`, className: We },
                    d &&
                      i().createElement(
                        "div",
                        { className: Ye },
                        i().createElement("div", { className: je }, d),
                        i().createElement(
                          "div",
                          { className: $e },
                          "(",
                          i().createElement("div", { className: Ge }, c),
                          "/",
                          o,
                          ")",
                        ),
                        e.value.tooltipDescription &&
                          i().createElement(
                            Pe,
                            {
                              header: e.value.tooltipTitle || void 0,
                              body: e.value.tooltipDescription,
                            },
                            i().createElement("div", { className: ze }),
                          ),
                      ),
                    e.value.items.map((e) => {
                      const a = e.value,
                        o = $(a, r),
                        s = $(a, n);
                      return i().createElement(
                        xe,
                        Ue({ key: a.id }, a, {
                          onClick: t,
                          selected: s,
                          isEquipped: o,
                          onNewComponentHover: u,
                        }),
                      );
                    }),
                    l,
                  );
                }),
              ),
          ),
          Ve = "Tabs_base_d9",
          qe = "Tabs_base__vertical_c0",
          Ze = "Tabs_list_0a",
          Qe = "Tabs_list__centered_dc",
          Je = "Tabs_wrapper_2d",
          et = "Tabs_wrapper__centered_d8",
          tt = "Tabs_wrapper__vertical_a5";
        function ut() {
          return (
            (ut =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            ut.apply(this, arguments)
          );
        }
        const nt = "tabs-role";
        var rt;
        !(function (e) {
          ((e.LIST = "tabs-list"), (e.CONTENT = "tab-content"), (e.TAB = "tab-key"));
        })(rt || (rt = {}));
        class at extends o.Component {
          constructor(...e) {
            (super(...e),
              (this.tabsProps = {}),
              (this.elementsList = []),
              (this.tabsListIndex = null),
              (this.state = { activeKey: "", activeElements: [] }),
              (this._getFirstTabKey = (e) => {
                if (!e) return;
                const t = e.find((e) => e.props[rt.TAB]);
                return t && t.props[rt.TAB];
              }),
              (this.handleSetActiveKey = (e) => {
                (this.setState({ activeKey: e }),
                  this.props.onTabChange &&
                    this.props.onTabChange({ from: this.state.activeKey, to: e }));
              }));
          }
          componentDidMount() {
            const e = i().Children.toArray(this.props.children),
              t = e.findIndex((e) => e.props[nt] === rt.LIST);
            if (t < 0) return;
            const u =
              this.props.activeKey ||
              this._getFirstTabKey(i().Children.toArray(e[t].props.children));
            ((e[t] = i().cloneElement(e[t], {
              children: i()
                .Children.toArray(e[t].props.children)
                .map((e) => i().cloneElement(e, { key: e.props[rt.TAB] })),
            })),
              (this.elementsList = e),
              (this.tabsListIndex = t),
              this.handleSetActiveKey(u));
          }
          componentWillReceiveProps(e) {
            void 0 !== e.activeKey &&
              e.activeKey !== this.props.activeKey &&
              this.handleSetActiveKey(e.activeKey);
          }
          componentDidUpdate(e, t) {
            if (null === this.tabsListIndex) return;
            const u = i().Children.toArray(this.props.children)[this.tabsListIndex],
              n = u.props.children.reduce(
                (e, t, u) => ((e[u] = t.props), e),
                Object.assign({}, this.tabsProps),
              ),
              o =
                ((s = this.tabsProps),
                (l = n),
                !(
                  Object.keys(s).length === Object.keys(l).length &&
                  Object.keys(s).every(
                    (e) => Object.prototype.hasOwnProperty.call(l, e) && s[e] === l[e],
                  )
                ));
            var s, l;
            const c = r()(
                Je,
                u.props.className,
                this.props.isTabsCentered && et,
                this.props.isVerticalTabs && tt,
              ),
              d = r()(Ze, this.props.isTabsCentered && Qe);
            if (t.activeKey !== this.state.activeKey || o) {
              const e = this.elementsList.findIndex((e) => {
                  if (e.props[nt] === rt.CONTENT)
                    return e.props[rt.TAB].includes(this.state.activeKey);
                }),
                t = this.elementsList.filter((t, u) => [this.tabsListIndex, e].includes(u)),
                r = t[0].props.children,
                o = r.map((e, t) =>
                  i().cloneElement(
                    e,
                    Object.assign(
                      {},
                      n[t],
                      { key: t, isActive: this.state.activeKey === e.props[rt.TAB] },
                      this.props.isVerticalTabs
                        ? {}
                        : { isFirst: 0 === t, isLast: t === r.length - 1 },
                      {
                        onClick: (e) => {
                          const u = n[t][rt.TAB];
                          this.state.activeKey === u ||
                            (n[t].onClick && n[t].onClick(e),
                            this.handleSetActiveKey(u),
                            this.props.onClickSound && a(this.props.onClickSound));
                        },
                        onMouseEnter: (e) => {
                          (n[t].onMouseEnter && n[t].onMouseEnter(e),
                            this.props.onMouseEnterSound && a(this.props.onMouseEnterSound));
                        },
                      },
                    ),
                  ),
                );
              ((this.tabsProps = n),
                this.setState({
                  activeElements: [
                    i().createElement(
                      "div",
                      { className: d, key: rt.LIST },
                      i().createElement("div", ut({}, u.props, { className: c }), o),
                    ),
                    t[1],
                  ],
                }));
            }
          }
          render() {
            const e = this.state.activeElements,
              t = r()(Ve, this.props.isVerticalTabs && qe);
            return i().createElement("div", { className: t }, e);
          }
        }
        at.defaultProps = {
          onClickSound: R.sounds.play(),
          onMouseEnterSound: R.sounds.highlight(),
        };
        const ot = [
          "children",
          "className",
          "activeKey",
          "onClickSound",
          "onMouseEnterSound",
          "isTabsCentered",
        ];
        function it() {
          return (
            (it =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            it.apply(this, arguments)
          );
        }
        const st = (e) => {
            let t = e.children,
              u = e.className,
              n = e.activeKey,
              r = e.onClickSound,
              a = e.onMouseEnterSound,
              o = e.isTabsCentered,
              s = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  r = {},
                  a = Object.keys(e);
                for (n = 0; n < a.length; n++) ((u = a[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
                return r;
              })(e, ot);
            return i().createElement(
              "div",
              it({ className: u }, s),
              i().createElement(
                at,
                { activeKey: n, onClickSound: r, onMouseEnterSound: a, isTabsCentered: o },
                t,
              ),
            );
          },
          lt = ({ children: e, component: t, props: u = {} }) =>
            t ? i().createElement(t, u, e) : e || null,
          ct = "Tab_base_dd",
          dt = "Tab_base__first_4a",
          mt = "Tab_base__last_96",
          Et = "Tab_base__medium_ec",
          _t = "Tab_base__active_5d",
          gt = "Tab_divider_ca",
          At = "Tab_divider__show_62",
          ht = "Tab_state_6c",
          pt = "Tab_stateHighlight_1e",
          Ft = "Tab_stateBorder_64",
          bt = "Tab_stateBorder__positionLeft_e7",
          Dt = "Tab_stateBorder__positionRight_db",
          vt = "Tab_counter_e1",
          Ct = [
            "isActive",
            "isFirst",
            "isLast",
            "isMedium",
            "isNotified",
            "children",
            "wrapper",
            "counter",
          ];
        function ft() {
          return (
            (ft =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            ft.apply(this, arguments)
          );
        }
        const Bt = (0, o.memo)((e) => {
            let t = e.isActive,
              u = void 0 !== t && t,
              n = e.isFirst,
              a = void 0 !== n && n,
              o = e.isLast,
              s = void 0 !== o && o,
              l = e.isMedium,
              c = void 0 !== l && l,
              d = e.isNotified,
              m = void 0 !== d && d,
              E = e.children,
              _ = void 0 === E ? "Tab" : E,
              g = e.wrapper,
              A = void 0 === g ? {} : g,
              h = e.counter,
              p = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  r = {},
                  a = Object.keys(e);
                for (n = 0; n < a.length; n++) ((u = a[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
                return r;
              })(e, Ct);
            return i().createElement(
              lt,
              A,
              i().createElement(
                "div",
                ft({ className: r()(ct, { [_t]: u }, { [dt]: a }, { [mt]: s }, { [Et]: c }) }, p),
                i().createElement(
                  "span",
                  { className: ht },
                  i().createElement("span", { className: pt }),
                  i().createElement("span", { className: r()(Ft, bt) }),
                  i().createElement("span", { className: r()(Ft, Dt) }),
                ),
                _,
                !s && !u && i().createElement("span", { className: r()(gt, At) }),
                (Boolean(h) || m) &&
                  i().createElement(
                    "div",
                    { className: vt },
                    i().createElement(ie, { value: h, isEmpty: m }),
                  ),
              ),
            );
          }),
          wt = "Header_base_eb",
          yt = "Header_titleWrapper_ab",
          St = "Header_title_e8",
          kt = "Header_infoButtonWrapper_e1",
          xt = "Header_infoIcon_8c",
          Lt = Object.keys(N)
            .filter((e) => !isNaN(Number(e)))
            .map((e) => Number(e)),
          Tt = {
            [N.Engraving]: R.strings.dogtags.customization.tab.engraving(),
            [N.Background]: R.strings.dogtags.customization.tab.background(),
          },
          Nt = systemLocale.toUpperCase(R.strings.dogtags.customization.mainTitle()),
          Rt = R.strings.dogtags.customization.infoTooltip(),
          Mt = {
            width: 10 * Math.max(...Lt.map((e) => Tt[e].length)) + "rem",
            padding: "0 5rem",
            flex: "0 0 150rem",
            justifyContent: "center",
          },
          Ot = (0, o.memo)(({ onTabClick: e, onInfoClick: t }) => {
            const u = T("model"),
              n = u.tab,
              r = u.newBackgroundComponentCount,
              a = u.newEngravingComponentCount;
            return i().createElement(
              "div",
              { className: wt },
              i().createElement(
                "div",
                { className: yt },
                i().createElement("p", { className: St }, Nt),
                i().createElement(
                  "div",
                  { className: kt },
                  i().createElement(
                    Pe,
                    { body: Rt },
                    i().createElement(
                      m,
                      { type: "ghost", onClick: t },
                      i().createElement("div", { className: xt }),
                    ),
                  ),
                ),
              ),
              i().createElement(
                st,
                { key: n, activeKey: String(n), onClickSound: R.sounds.dt_tab() },
                i().createElement(
                  "div",
                  { "tabs-role": rt.LIST },
                  Lt.map((t) => {
                    const u = { [N.Engraving]: a, [N.Background]: r }[t] || 0;
                    return i().createElement(
                      Bt,
                      {
                        key: String(t),
                        "tabs-role": rt.TAB,
                        "tab-key": String(t),
                        onClick: e,
                        style: Mt,
                        counter: u,
                      },
                      Tt[t],
                    );
                  }),
                ),
              ),
            );
          }),
          It = (e, t) => {
            const u = t.split("."),
              n = u[0];
            if (!e || "object" != typeof e)
              return (
                console.warn(`Reference "${JSON.stringify(e, null, 2)}" is not a valid object.`),
                !1
              );
            if (!n) return (console.warn(`Invalid key "${n}" in path ${t}.`), !1);
            if (!(n in e))
              return (
                console.warn(
                  `Key "${n}" was not found in reference "${JSON.stringify(e, null, 2)}".`,
                ),
                !1
              );
            const r = u.slice(1);
            return 0 === r.length || It(e[n], r.join("."));
          },
          Pt = [
            "model.equippedDogTag",
            "model.equippedDogTag.background",
            "model.equippedDogTag.engraving",
            "model.engravingGrid",
            "model.backgroundGrid",
          ];
        Pt.forEach((e) => It(window, e));
        const Ht = () => (
            T(Pt[0]),
            T(Pt[1]),
            T(Pt[2]),
            T(Pt[3]),
            T(Pt[4]),
            ((e, t = !0) => {
              if (!It(window, e)) throw Error(`Path "${e}" does not exist.`);
              const u = T(e, t ? L.Deep : L.None);
              return "object" == typeof u && null !== u
                ? (0, B.lw)(u)
                : (t &&
                    console.warn(
                      `Tracking of primitive value ${String(u)} in ${e} is not supported.`,
                    ),
                  u);
            })("model")
          ),
          Wt = (e) => {
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
          Xt = (e) => {
            if (!e) return !1;
            const t = e.getBoundingClientRect(),
              u = t.width,
              n = t.height;
            return 0 !== u && 0 !== n;
          },
          Yt = (e) => {
            const t = (0, o.useState)(Xt(e ? e.current : null)),
              u = t[0],
              n = t[1];
            return (
              (0, o.useEffect)(() => {
                let t = 0;
                const u = () => {
                  t = requestAnimationFrame(() => {
                    Xt(e ? e.current : null) ? n(!0) : u();
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
        var jt = u(380),
          Gt = u.n(jt);
        const $t = "ScrollArea_base_47",
          zt = "ScrollArea_base__scrollIndent_1d",
          Ut = "ScrollArea_base__verticalScrollbarMargin_50",
          Kt = "ScrollArea_base__multiple_44",
          Vt = "ScrollArea_base__hidden_ec",
          qt = i().forwardRef((e, t) => {
            const u = e.offsetLeft,
              n = void 0 === u ? 0 : u,
              a = e.offsetTop,
              s = void 0 === a ? 0 : a,
              l = e.scrollSettings,
              c = e.onUpdateActiveAxis,
              d = e.onHorizontalScroll,
              m = e.onVerticalScroll,
              E = e.onOverScrollAtBeginning,
              _ = e.onOverScrollAtEnd,
              g = e.wrapperIndent,
              A = e.verticalScrollbarMargin,
              h = e.isMultipleScroll,
              p = e.scrollAreaContainer,
              F = e.children,
              b = e.classMix,
              D = e.onScrollLeftHandled,
              v = (0, o.useState)(!1),
              C = v[0],
              f = v[1],
              B = (0, o.useState)(),
              w = B[0],
              y = B[1],
              S = (0, o.useState)(),
              k = S[0],
              x = S[1],
              L = (0, o.useRef)(null),
              T = (0, o.useCallback)(() => {
                w &&
                  c &&
                  c(
                    { x: w.scrollbarXActive, y: w.scrollbarYActive },
                    { x: w.reach.x, y: w.reach.y },
                  );
              }, [c, w]),
              N = (0, o.useCallback)(() => w, [w]),
              R = (0, o.useCallback)(() => {
                w && w.update();
              }, [w]),
              M = (0, o.useCallback)(
                (e, t, u) => {
                  w && (w.setScrollLeft(e, t, u), D && D(e, w.contentWidth - w.containerWidth));
                },
                [w, D],
              ),
              O = (0, o.useCallback)(
                (e) => {
                  w &&
                    (w.setScrollLeftImmediately(e), D && D(e, w.contentWidth - w.containerWidth));
                },
                [w, D],
              ),
              I = (0, o.useCallback)(
                (e, t, u) => {
                  w && w.setScrollTop(e, t, u);
                },
                [w],
              ),
              P = (0, o.useCallback)(
                (e) => {
                  w && w.setScrollTopImmediately(e);
                },
                [w],
              ),
              H = (0, o.useCallback)(() => {
                if (k && d && w) {
                  const e = {
                    scrollPosition: k.scrollLeft < 0 ? 0 : k.scrollLeft,
                    reach: w.reach.x,
                  };
                  d(e);
                }
              }, [d, k, w]),
              W = (0, o.useCallback)(() => {
                if (k && m && w) {
                  const e = { scrollPosition: k.scrollTop, reach: w.reach.y };
                  m(e);
                }
              }, [m, k, w]),
              X = (0, o.useCallback)(() => {
                E && E();
              }, [E]),
              Y = (0, o.useCallback)(() => {
                _ && _();
              }, [_]),
              j = (0, o.useCallback)(
                (e) => {
                  ("function" == typeof t ? t(e) : null !== t && (t.current = e), x(e));
                },
                [t],
              ),
              G = (0, o.useCallback)(() => {
                w &&
                  (w.update(),
                  (L.current = Wt(() => {
                    T();
                  })));
              }, [w, T]),
              $ = (0, o.useCallback)((e) => {
                0 === e.screenX &&
                  0 === e.screenY &&
                  (e.stopImmediatePropagation(), e.preventDefault());
              }, []);
            (0, o.useEffect)(() => {
              if (w && k)
                return (
                  document.addEventListener("mousemove", $),
                  window.addEventListener("resize", G),
                  k.addEventListener("ps-scroll-x", H),
                  k.addEventListener("ps-scroll-y", W),
                  k.addEventListener("over-scroll-beginning", X),
                  k.addEventListener("over-scroll-ending", Y),
                  f(!0),
                  () => {
                    (window.removeEventListener("resize", G),
                      document.removeEventListener("mousemove", $),
                      k &&
                        (k.removeEventListener("ps-scroll-x", H),
                        k.removeEventListener("ps-scroll-y", W),
                        k.removeEventListener("over-scroll-beginning", X),
                        k.removeEventListener("over-scroll-ending", Y)));
                  }
                );
            }, [$, H, X, Y, G, k, w, W]);
            const z = (0, o.useRef)(k || null);
            z.current = k || null;
            const U = Yt(z);
            ((0, o.useEffect)(
              () => (
                !w && k && U && y(new (Gt())(k, Object.assign({}, l))),
                () => {
                  w && (w.destroy(), y(void 0));
                }
              ),
              [k, U, l, w],
            ),
              (0, o.useEffect)(
                () => () => {
                  null == L.current || L.current();
                },
                [],
              ),
              (0, o.useEffect)(
                () =>
                  Wt(() => {
                    w && T();
                  }),
                [T, w],
              ),
              (0, o.useEffect)(() => {
                n > 0 && O(n);
              }, [n, O]),
              (0, o.useEffect)(() => {
                s > 0 && P(s);
              }, [s, P]),
              (0, o.useEffect)(() => {
                p &&
                  ((p.setScrollLeft = M),
                  (p.setScrollTop = I),
                  (p.setScrollLeftImmediately = O),
                  (p.setScrollTopImmediately = P),
                  (p.updateScrollArea = R),
                  (p.getScrollbar = N));
              }, [p, M, O, I, P, R, N]));
            const K = r()($t, { [zt]: g, [Vt]: !C, [Ut]: A, [Kt]: h }, b);
            return i().createElement("div", { className: K, ref: j }, F);
          }),
          Zt = "Router_base_17",
          Qt = "Router_innerWrapper_d8",
          Jt = "Router_gridWrapper_c2",
          eu = "Router_infoWrapper_95",
          tu = "Router_dogtagsWrapper_02",
          uu = "Router_dogtagsInfoWrapper_b7",
          nu = "Router_customizationWrapper_05",
          ru = "Router_scrollAreaWrapper_93",
          au = "Router_scrollAreaWrapper_bottomMask_63",
          ou = "Router_gridTitle_a2",
          iu = "Router_subNavigation_b2",
          su = "Router_topDivider_23",
          lu = "Router_gridBottomSeparator_13",
          cu = {
            handlers: ["click-rail", "drag-thumb", "keyboard", "wheel"],
            suppressScrollX: !0,
            wheelSpeed: 6,
            wheelPropagation: !0,
            useBothWheelAxes: !0,
          },
          du = { dedication: !0, season: !0, triumph: !0, static: !0 },
          mu = {
            [N.Engraving]: R.strings.dogtags.customization.tab.engraving(),
            [N.Background]: R.strings.dogtags.customization.tab.background(),
          },
          Eu = () => {
            const e = Ht(),
              t = e.onEquip,
              u = e.onNewComponentHover,
              n = e.tab,
              a = e.equippedDogTag,
              s = a.playerName,
              l = a.clanTag,
              c = a.engraving.id,
              d = a.background.id,
              m = e.engravingGrid,
              E = e.backgroundGrid,
              _ = e.newEngravingSkillCount,
              g = e.newEngravingDedicationCount,
              A = e.newEngravingTriumphCount,
              h = e.newEngravingStaticCount,
              p = (0, o.useState)({ background: d, engraving: c }),
              F = p[0],
              b = p[1],
              D = {
                background: te(E, F.background) || E[0].value.items[0].value,
                engraving: te(m, F.engraving) || m[0].value.items[0].value,
              },
              v = {
                engraving: te(m, c) || m[0].value.items[0].value,
                background: te(E, d) || E[0].value.items[0].value,
              },
              C = (0, o.useState)(du),
              f = C[0],
              B = C[1],
              w = (0, o.useState)(!1),
              y = w[0],
              S = w[1],
              k = (0, o.useState)(!0),
              x = k[0],
              L = k[1],
              T = ((e, t) => e[ee[t]])(D, n),
              R = mu[n],
              M = ((e, t) => e[J[t]])({ backgroundGrid: E, engravingGrid: m }, n),
              O =
                n === N.Engraving
                  ? ((e, t) => {
                      const u = Q(t).reduce((e, t) => (e.push(...H[t]), e), []);
                      return Z(
                        e.map((e) =>
                          Object.assign({}, e, {
                            value: Object.assign({}, e.value, {
                              items: e.value.items.filter((e) => u.includes(e.value.purpose)),
                            }),
                          }),
                        ),
                      );
                    })(M, f)
                  : M,
              X = Z(
                O.map((e) =>
                  Object.assign({}, e, {
                    value: Object.assign({}, e.value, {
                      items: e.value.items.filter((e) => !e.value.isLocked),
                    }),
                  }),
                ),
              );
            const Y = ue(X),
              j =
                n === N.Engraving
                  ? ((e) =>
                      [P.Dedication, P.Season, P.Triumph, P.Static].filter((t) => {
                        for (let u = 0; u < e.length; u++) {
                          const n = e[u].value.items[0];
                          if (n && H[t].includes(n.value.purpose)) return !0;
                        }
                        return !1;
                      }))(M)
                  : [],
              G = (0, o.useMemo)(() => ({ gridData: y ? X : O, totalItems: ue(O) }), [X, O, y]),
              $ = G.gridData,
              z = G.totalItems,
              U = (0, o.useCallback)(
                (e, u) => {
                  const n = { engraving: c, background: d };
                  ((n[e] = u), t(n));
                },
                [t, c, d],
              ),
              K = (0, o.useCallback)(
                (e) => {
                  (b((t) => Object.assign({}, t, { [e.type]: e.id })),
                    e.isLocked || U(e.type, e.id));
                },
                [U],
              ),
              V = (0, o.useCallback)(
                (e) => {
                  b((t) => Object.assign({}, t, { [e]: v[e].id }));
                },
                [v],
              ),
              q = (0, o.useCallback)((e) => {
                L(e.y);
              }, []),
              ne = (0, o.useCallback)((e) => {
                L("end" !== e.reach);
              }, []),
              re = (0, o.useCallback)(() => {
                (B({ dedication: !0, season: !0, triumph: !0, static: !0 }), S(!1));
              }, []),
              ae = Q(f),
              oe = ((e) => {
                const t = e.background,
                  u = e.engraving,
                  n = t.currentGrade + 1,
                  r = u.currentGrade + 1;
                return (
                  (u.purpose === I.Triumph && 4 === r) ||
                  r === W ||
                  (u.purpose === I.Static && u.currentProgress <= u.lightingUpTo) ||
                  n === W
                );
              })(D),
              ie = r()(ru, x && au);
            return i().createElement(
              "div",
              { className: Zt },
              i().createElement(
                "div",
                { className: Qt },
                i().createElement(
                  "div",
                  { className: Jt },
                  i().createElement(
                    "div",
                    { className: iu },
                    i().createElement("div", { className: ou }, systemLocale.toUpperCase(R)),
                    i().createElement(Ya, {
                      newEngravingSkillCount: _,
                      newEngravingDedicationCount: g,
                      newEngravingTriumphCount: A,
                      newEngravingStaticCount: h,
                      availablePurposeGroups: j,
                      setPurposeGroupFilters: B,
                      purposeGroupFilters: f,
                      showOnlyAvailableItems: y,
                      setShowOnlyAvailableItems: S,
                      availableItemsCount: Y,
                    }),
                    i().createElement("div", { className: su }),
                  ),
                  $.length > 0
                    ? i().createElement(
                        "div",
                        { className: ie },
                        i().createElement(
                          qt,
                          {
                            key: `${n}-${ae.join("-")}-${String(y)}`,
                            scrollSettings: cu,
                            onUpdateActiveAxis: q,
                            onVerticalScroll: ne,
                            verticalScrollbarMargin: !0,
                          },
                          i().createElement(Ke, {
                            data: $,
                            count: z,
                            onItemSelect: K,
                            onNewComponentHover: u,
                            selectedItems: D,
                            equippedItems: v,
                          }),
                        ),
                      )
                    : i().createElement(za, { clearFilters: re }),
                  i().createElement("div", { className: lu }),
                ),
                i().createElement(
                  "div",
                  { className: eu },
                  i().createElement(
                    "div",
                    { className: tu },
                    i().createElement(Aa, {
                      playerName: s,
                      clanTag: l,
                      background: D.background,
                      engraving: D.engraving,
                      isHighlighted: oe,
                    }),
                  ),
                  i().createElement(
                    "div",
                    { className: uu },
                    i().createElement(
                      qt,
                      {
                        key: JSON.stringify({ currentSelectedItem: T, equippedDogTag: v }),
                        scrollSettings: cu,
                      },
                      i().createElement(Ir, { currentItem: T }),
                    ),
                  ),
                  i().createElement(
                    "div",
                    { className: nu },
                    i().createElement(oo, { selectedItems: D, equippedItems: v, onItemReset: V }),
                  ),
                ),
              ),
            );
          },
          _u = "DogtagsInfo_base_68",
          gu = "DogtagsInfo_title_02",
          Au = "DogtagsInfo_progressBarWrapper_48",
          hu = "DogtagsInfo_currentLevel_14",
          pu = "DogtagsInfo_nextLevel_53",
          Fu = "DogtagsInfo_valuesWrapper_ac",
          bu = "DogtagsInfo_valuesWrapper_inner_55",
          Du = "DogtagsInfo_valuesWrapper__locked_59",
          vu = "DogtagsInfo_currentValue_25",
          Cu = "DogtagsInfo_totalValue_47",
          fu = "DogtagsInfo_valuesSeparator_db",
          Bu = "DogtagsInfo_medalInfo_0d",
          wu = "DogtagsInfo_skillInfo_13",
          yu = "DogtagsInfo_skillInfoIcon_f9",
          Su = "DogtagsInfo_shieldLevelWrapper_fa",
          ku = "DogtagsInfo_single_86",
          xu = "DogtagsInfo_currentShieldWrapper_b0",
          Lu = "DogtagsInfo_nextShieldWrapper_7e",
          Tu = "DogtagsInfo_currentLevelShield_60",
          Nu = "DogtagsInfo_currentLevelValue_d5",
          Ru = "DogtagsInfo_nextLevelValue_d5",
          Mu = "DogtagsInfo_arrowLock_6a",
          Ou = "DogtagsInfo_nextLevelShield_22",
          Iu = "DogtagsInfo_infoSeparator_d7",
          Pu = "DogtagsInfo_lockedText_9d",
          Hu = "DogtagsInfo_lockedIcon_04",
          Wu = "DogtagsInfo_skillDescriptionWrapper_dc",
          Xu = "DogtagsInfo_skillDescription_94",
          Yu = "DogtagsInfo_skillInfoBorderTop_62",
          ju = "DogtagsInfo_skillInfoBorderBottom_50",
          Gu = "DogtagsInfo_currentProgress_86";
        var $u = u(887),
          zu = u.n($u);
        const Uu = (e, t, u) =>
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
        var Ku = u(67);
        const Vu = {
          extraLarge: { weight: 4, width: 2560, height: 1440 },
          large: { weight: 3, width: 1920, height: 1080 },
          medium: { weight: 2, width: 1600, height: 900 },
          small: { weight: 1, width: 1366, height: 768 },
          extraSmall: { weight: 0, width: 1024, height: 768 },
        };
        var qu;
        function Zu(e, t, u) {
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
            a = Math.min(n, r);
          return {
            extraLarge: a === u.extraLarge.weight,
            large: a === u.large.weight,
            medium: a === u.medium.weight,
            small: a === u.small.weight,
            extraSmall: a === u.extraSmall.weight,
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
        })(qu || (qu = {}));
        const Qu = Ku.O.client.getSize("rem"),
          Ju = Qu.width,
          en = Qu.height,
          tn = Object.assign({ width: Ju, height: en }, Zu(Ju, en, Vu)),
          un = (0, o.createContext)(tn),
          nn = ["children"];
        const rn = (e) => {
          let t = e.children,
            u = (function (e, t) {
              if (null == e) return {};
              var u,
                n,
                r = {},
                a = Object.keys(e);
              for (n = 0; n < a.length; n++) ((u = a[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
              return r;
            })(e, nn);
          const n = (0, o.useContext)(un),
            r = n.extraLarge,
            a = n.large,
            i = n.medium,
            s = n.small,
            l = n.extraSmall,
            c = n.extraLargeWidth,
            d = n.largeWidth,
            m = n.mediumWidth,
            E = n.smallWidth,
            _ = n.extraSmallWidth,
            g = n.extraLargeHeight,
            A = n.largeHeight,
            h = n.mediumHeight,
            p = n.smallHeight,
            F = n.extraSmallHeight,
            b = { extraLarge: g, large: A, medium: h, small: p, extraSmall: F };
          if (u.extraLarge || u.large || u.medium || u.small || u.extraSmall) {
            if (u.extraLarge && r) return t;
            if (u.large && a) return t;
            if (u.medium && i) return t;
            if (u.small && s) return t;
            if (u.extraSmall && l) return t;
          } else {
            if (u.extraLargeWidth && c) return Uu(t, u, b);
            if (u.largeWidth && d) return Uu(t, u, b);
            if (u.mediumWidth && m) return Uu(t, u, b);
            if (u.smallWidth && E) return Uu(t, u, b);
            if (u.extraSmallWidth && _) return Uu(t, u, b);
            if (!(
              u.extraLargeWidth ||
              u.largeWidth ||
              u.mediumWidth ||
              u.smallWidth ||
              u.extraSmallWidth
            )) {
              if (u.extraLargeHeight && g) return t;
              if (u.largeHeight && A) return t;
              if (u.mediumHeight && h) return t;
              if (u.smallHeight && p) return t;
              if (u.extraSmallHeight && F) return t;
            }
          }
          return null;
        };
        rn.defaultProps = {
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
        ((0, o.memo)(rn),
          (0, o.memo)(({ children: e }) => {
            const t = (0, o.useContext)(un),
              u = (0, o.useState)(t),
              n = u[0],
              r = u[1],
              a = (0, o.useCallback)((e, t) => {
                const u = Ku.O.view.pxToRem(e),
                  n = Ku.O.view.pxToRem(t);
                r(Object.assign({ width: u, height: n }, Zu(u, n, Vu)));
              }, []);
            (f(() => {
              engine.on("clientResized", a);
            }),
              (0, o.useEffect)(() => () => engine.off("clientResized", a), [a]));
            const s = (0, o.useMemo)(() => Object.assign({}, n), [n]);
            return i().createElement(un.Provider, { value: s }, e);
          }));
        let an, on, sn;
        (!(function (e) {
          ((e[(e.ExtraSmall = Vu.extraSmall.width)] = "ExtraSmall"),
            (e[(e.Small = Vu.small.width)] = "Small"),
            (e[(e.Medium = Vu.medium.width)] = "Medium"),
            (e[(e.Large = Vu.large.width)] = "Large"),
            (e[(e.ExtraLarge = Vu.extraLarge.width)] = "ExtraLarge"));
        })(an || (an = {})),
          (function (e) {
            ((e[(e.ExtraSmall = Vu.extraSmall.width)] = "ExtraSmall"),
              (e[(e.Small = Vu.small.width)] = "Small"),
              (e[(e.Medium = Vu.medium.width)] = "Medium"),
              (e[(e.Large = Vu.large.width)] = "Large"),
              (e[(e.ExtraLarge = Vu.extraLarge.width)] = "ExtraLarge"));
          })(on || (on = {})),
          (function (e) {
            ((e[(e.ExtraSmall = Vu.extraSmall.height)] = "ExtraSmall"),
              (e[(e.Small = Vu.small.height)] = "Small"),
              (e[(e.Medium = Vu.medium.height)] = "Medium"),
              (e[(e.Large = Vu.large.height)] = "Large"),
              (e[(e.ExtraLarge = Vu.extraLarge.height)] = "ExtraLarge"));
          })(sn || (sn = {})));
        const ln = () => {
            const e = (0, o.useContext)(un),
              t = e.width,
              u = e.height,
              n = ((e) => {
                switch (!0) {
                  case e.extraLarge:
                    return an.ExtraLarge;
                  case e.large:
                    return an.Large;
                  case e.medium:
                    return an.Medium;
                  case e.small:
                    return an.Small;
                  case e.extraSmall:
                    return an.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), an.ExtraSmall);
                }
              })(e),
              r = ((e) => {
                switch (!0) {
                  case e.extraLargeWidth:
                    return on.ExtraLarge;
                  case e.largeWidth:
                    return on.Large;
                  case e.mediumWidth:
                    return on.Medium;
                  case e.smallWidth:
                    return on.Small;
                  case e.extraSmallWidth:
                    return on.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), on.ExtraSmall);
                }
              })(e),
              a = ((e) => {
                switch (!0) {
                  case e.extraLargeHeight:
                    return sn.ExtraLarge;
                  case e.largeHeight:
                    return sn.Large;
                  case e.mediumHeight:
                    return sn.Medium;
                  case e.smallHeight:
                    return sn.Small;
                  case e.extraSmallHeight:
                    return sn.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), sn.ExtraSmall);
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
          cn = ["xl", "lg", "md", "sm", "xs"],
          dn = (e) => e.includes("_") && ((e) => cn.includes(e))(e.split("_").at(-1)),
          mn = [an.ExtraLarge, an.Large, an.Medium, an.Small, an.ExtraSmall],
          En = (e, t) =>
            Object.keys(e).reduce((u, n) => {
              if (n in u) return u;
              if (dn(n)) {
                const r = n.split("_").slice(0, -1).join("_");
                if (r in u) return u;
                const a = mn.indexOf(t),
                  o = (-1 !== a ? cn.slice(a) : [])
                    .map((e) => r + "_" + e)
                    .find((t) => void 0 !== e[t]),
                  i = o ? e[o] : void 0;
                return ((u[r] = void 0 !== i ? i : e[r]), u);
              }
              const r = e[n];
              return (
                void 0 === r ||
                  ((e, t) => cn.some((u) => void 0 !== t[`${e}_${u}`]))(n, e) ||
                  (u[n] = r),
                u
              );
            }, {}),
          _n = (e, t = En) => {
            const u = (
              (e, t = En) =>
              (u) => {
                const n = ln().mediaSize,
                  r = (0, o.useMemo)(() => t(u, n), [u, n]);
                return i().createElement(e, r);
              }
            )(e, t);
            return i().memo((t) =>
              Object.keys(t).some((e) => dn(e) && void 0 !== t[e])
                ? i().createElement(u, t)
                : i().createElement(e, t),
            );
          },
          gn = {
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
          An = [
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
        function hn() {
          return (
            (hn =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            hn.apply(this, arguments)
          );
        }
        Object.keys(zu());
        const pn = {
            XL: { mt: gn.mt__XL, mr: gn.mr__XL, mb: gn.mb__XL, ml: gn.ml__XL },
            LG: { mt: gn.mt__LG, mr: gn.mr__LG, mb: gn.mb__LG, ml: gn.ml__LG },
            MDp: { mt: gn.mt__MDp, mr: gn.mr__MDp, mb: gn.mb__MDp, ml: gn.ml__MDp },
            MD: { mt: gn.mt__MD, mr: gn.mr__MD, mb: gn.mb__MD, ml: gn.ml__MD },
            SMp: { mt: gn.mt__SMp, mr: gn.mr__SMp, mb: gn.mb__SMp, ml: gn.ml__SMp },
            SM: { mt: gn.mt__SM, mr: gn.mr__SM, mb: gn.mb__SM, ml: gn.ml__SM },
            XS: { mt: gn.mt__XS, mr: gn.mr__XS, mb: gn.mb__XS, ml: gn.ml__XS },
          },
          Fn = (Object.keys(pn), ["mt", "mr", "mb", "ml"]),
          bn = { mt: "marginTop", mr: "marginRight", mb: "marginBottom", ml: "marginLeft" },
          Dn = _n((e) => {
            let t = e.className,
              u = e.width,
              n = e.height,
              a = e.m,
              s = e.mt,
              l = void 0 === s ? a : s,
              c = e.mr,
              d = void 0 === c ? a : c,
              m = e.mb,
              E = void 0 === m ? a : m,
              _ = e.ml,
              g = void 0 === _ ? a : _,
              A = e.column,
              h = e.row,
              p = e.flexDirection,
              F = void 0 === p ? (A ? "column" : h && "row") || void 0 : p,
              b = e.flexStart,
              D = e.center,
              v = e.flexEnd,
              C = e.spaceBetween,
              f = e.spaceAround,
              B = e.justifyContent,
              w =
                void 0 === B
                  ? (b ? "flex-start" : D && "center") ||
                    (v && "flex-end") ||
                    (C && "space-between") ||
                    (f && "space-around") ||
                    void 0
                  : B,
              y = e.alignItems,
              S =
                void 0 === y
                  ? (b ? "flex-start" : D && "center") || (v && "flex-end") || void 0
                  : y,
              k = e.alignSelf,
              x = e.wrap,
              L = e.flexWrap,
              T = void 0 === L ? (x ? "wrap" : void 0) : L,
              N = e.grow,
              R = e.shrink,
              M = e.flex,
              O = void 0 === M ? (N || R ? `${N ? 1 : 0} ${R ? 1 : 0} auto` : void 0) : M,
              I = e.style,
              P = e.children,
              H = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  r = {},
                  a = Object.keys(e);
                for (n = 0; n < a.length; n++) ((u = a[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
                return r;
              })(e, An);
            const W = (0, o.useMemo)(() => {
                const e = { mt: l, mr: d, mb: E, ml: g },
                  t = ((e) =>
                    Fn.reduce((t, u) => {
                      const n = e[u];
                      return n && "number" != typeof n ? t.concat(pn[!0 === n ? "MD" : n][u]) : t;
                    }, []))(e),
                  r = ((e) =>
                    Fn.reduce((t, u) => {
                      const n = e[u];
                      return ("number" == typeof n && (t[bn[u]] = n + "rem"), t);
                    }, {}))(e);
                return {
                  computedStyle: Object.assign({}, I, r, {
                    width: void 0 !== u && "number" == typeof u ? u + "rem" : u,
                    height: void 0 !== n && "number" == typeof n ? n + "rem" : n,
                    flex: O,
                    alignSelf: k,
                    display: F || S ? "flex" : void 0,
                    flexDirection: F,
                    flexWrap: T,
                    justifyContent: w,
                    alignItems: S,
                  }),
                  computedClassNames: t,
                };
              }, [u, n, l, d, E, g, I, O, k, F, T, w, S]),
              X = W.computedStyle,
              Y = W.computedClassNames;
            return i().createElement(
              "div",
              hn({ className: r()(gn.base, ...Y, t), style: X }, H),
              P,
            );
          });
        let vn;
        !(function (e) {
          ((e[(e.left = 0)] = "left"), (e[(e.right = 1)] = "right"));
        })(vn || (vn = {}));
        const Cn = (e, t, u) => {
            if (u % 2) {
              const u = e.pop();
              return [...e, u + t];
            }
            return [...e, t];
          },
          fn = (e, t, u) => {
            if (0 === u) return [t];
            if (u % 2) return [...e, " " === t ? " " : t];
            {
              const u = e.pop();
              return [...e, u + t];
            }
          },
          Bn = (e, t, u = vn.left) => e.split(t).reduce(u === vn.left ? Cn : fn, []),
          wn = (() => {
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
          yn = ["zh_cn", "zh_sg", "zh_tw"],
          Sn = (e, t = vn.left) => {
            const u = R.strings.settings.LANGUAGE_CODE().toLowerCase();
            return yn.includes(u)
              ? wn(e)
              : ((e, t = vn.left) => {
                  let u = [];
                  const n =
                      /(?<=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])(\x2D)(?=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])/gu,
                    r = e.replace(/&nbsp;/g, " ");
                  return (Bn(r, /( )/, t).forEach((e) => (u = u.concat(Bn(e, n, vn.left)))), u);
                })(e, t);
          },
          kn = "FormatText_base_d0",
          xn = ({ binding: e, text: t = "", classMix: u, alignment: n = vn.left }) =>
            null === t
              ? (console.error("FormatText was supplied with 'null'"), null)
              : i().createElement(
                  o.Fragment,
                  null,
                  t.split("\n").map((t, a) =>
                    i().createElement(
                      "div",
                      { className: r()(kn, u), key: `${t}-${a}` },
                      ((e, t, u) =>
                        e
                          .split(/%\((.*?)\)(?:[sd])?/g)
                          .map((e) => (u && e in u ? u[e] : Sn(e, t))))(t, n, e).map((e, t) =>
                        i().createElement(o.Fragment, { key: `${t}-${e}` }, e),
                      ),
                    ),
                  ),
                );
        var Ln = u(532),
          Tn = u.n(Ln);
        const Nn = {
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
          Rn = [
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
        function Mn() {
          return (
            (Mn =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            Mn.apply(this, arguments)
          );
        }
        Object.keys(zu());
        const On = Object.keys(Tn()),
          In = { mt: "MD", mr: "SM", mb: "SM", ml: "SM" },
          Pn = { mt: "SM", mr: "XS", mb: "XS", ml: "XS" },
          Hn = { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          Wn = {
            XL: { mt: "XL", mr: "XL", mb: "XL", ml: "XL" },
            LG: { mt: "LG", mr: "LG", mb: "LG", ml: "LG" },
            MDp: { mt: "MDp", mr: "MDp", mb: "MDp", ml: "MDp" },
            MD: { mt: "MD", mr: "MD", mb: "MD", ml: "MD" },
            SMp: { mt: "SMp", mr: "SMp", mb: "SMp", ml: "SMp" },
            SM: { mt: "SM", mr: "SM", mb: "SM", ml: "SM" },
            XS: { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          },
          Xn =
            (Object.keys(Wn),
            {
              "heading-H144": { mt: "XL", mr: "LG", mb: "LG", ml: "LG" },
              "heading-H73": { mt: "LG", mr: "MD", mb: "MD", ml: "MD" },
              "heading-H56": In,
              "heading-H36": In,
              "heading-H28": Pn,
              "heading-H24": Pn,
              "heading-H24R": Pn,
              "heading-H22": Pn,
              "heading-H20R": Pn,
              "heading-H18": Pn,
              "heading-H15": Hn,
              "heading-H14": Hn,
              "paragraph-P24": Pn,
              "paragraph-P18": Pn,
              "paragraph-P16": Pn,
              "paragraph-P14": Hn,
              "paragraph-P12": Hn,
              "paragraph-P10": Hn,
            }),
          Yn =
            (Object.keys(Xn),
            (e) =>
              e
                ? ((e) => On.includes(e))(e)
                  ? { colorClassName: Nn[e] }
                  : { colorStyle: { color: e } }
                : {}),
          jn = _n((e) => {
            let t = e.text,
              u = e.variant,
              n = e.className,
              a = e.color,
              s = e.m,
              l = e.mt,
              c = void 0 === l ? s : l,
              d = e.mr,
              m = void 0 === d ? s : d,
              E = e.mb,
              _ = void 0 === E ? s : E,
              g = e.ml,
              A = void 0 === g ? s : g,
              h = e.style,
              p = e.format,
              F = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  r = {},
                  a = Object.keys(e);
                for (n = 0; n < a.length; n++) ((u = a[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
                return r;
              })(e, Rn);
            const b = (0, o.useMemo)(() => {
                const e = Yn(a),
                  t = e.colorClassName,
                  u = e.colorStyle,
                  n = void 0 === u ? {} : u;
                return { computedStyle: Object.assign({}, h, n), colorClassName: t };
              }, [h, a]),
              D = b.computedStyle,
              v = b.colorClassName;
            return i().createElement(
              Dn,
              Mn(
                {
                  className: r()(Nn.base, u && Nn[u], v, n),
                  style: D,
                  mt: !0 === c ? Xn[u || "paragraph-P16"].mt : c,
                  mr: !0 === m ? Xn[u || "paragraph-P16"].mr : m,
                  mb: !0 === _ ? Xn[u || "paragraph-P16"].mb : _,
                  ml: !0 === A ? Xn[u || "paragraph-P16"].ml : A,
                },
                F,
              ),
              void 0 !== p ? i().createElement(xn, Mn({}, p, { text: t })) : t,
            );
          }),
          Gn = (0, o.memo)(({ infoTitle: e, infoText: t, isLocked: u, unlockText: n }) =>
            i().createElement(
              "div",
              { className: _u },
              i().createElement(jn, { className: gu, text: e }),
              i().createElement(jn, { className: Bu, text: t }),
              u &&
                i().createElement(
                  i().Fragment,
                  null,
                  i().createElement("div", { className: Iu }),
                  i().createElement(
                    "div",
                    { className: Pu },
                    i().createElement("div", { className: Hu }),
                    i().createElement(jn, { text: n }),
                  ),
                ),
            ),
          ),
          $n = {
            base: "ProgressBar_base_45",
            base__medium: "ProgressBar_base__medium_62",
            base__small: "ProgressBar_base__small_df",
            background: "ProgressBar_background_51",
            background__medium: "ProgressBar_background__medium_6e",
            background__small: "ProgressBar_background__small_46",
            lineWrapper: "ProgressBar_lineWrapper_6a",
          };
        let zn, Un;
        (!(function (e) {
          ((e.Small = "small"), (e.Medium = "medium"), (e.Big = "big"), (e.Default = "big"));
        })(zn || (zn = {})),
          (function (e) {
            ((e[(e.Simple = 0)] = "Simple"), (e[(e.Growing = 1)] = "Growing"));
          })(Un || (Un = {})));
        const Kn = ({ size: e = zn.Default, classMix: t }) =>
            i().createElement("div", { className: r()($n.background, $n[`background__${e}`], t) }),
          Vn = {
            base: "ProgressBarBlink_base_24",
            base__medium: "ProgressBarBlink_base__medium_ec",
            base__small: "ProgressBarBlink_base__small_0f",
          },
          qn = ({ size: e }) => {
            const t = r()(Vn.base, Vn[`base__${e}`]);
            return i().createElement("div", { className: t });
          },
          Zn = {
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
          Qn = (0, o.memo)(
            ({
              size: e,
              lineRef: t,
              disabled: u,
              baseStyles: n,
              isComplete: a,
              withoutBounce: o,
            }) => {
              const s = r()(
                  Zn.base,
                  Zn[`base__${e}`],
                  u && Zn.base__disabled,
                  a && Zn.base__finished,
                  o && Zn.base__withoutBounce,
                ),
                l = !u && !a;
              return i().createElement(
                "div",
                { className: s, style: n, ref: t },
                i().createElement("div", { className: Zn.pattern }),
                i().createElement("div", { className: Zn.gradient }),
                l && i().createElement(qn, { size: e }),
              );
            },
          ),
          Jn = ({ size: e, value: t, lineRef: u, disabled: n, onComplete: r }) => {
            const a = (0, o.useMemo)(() => ({ width: `${t}%`, transitionProperty: "none" }), [t]),
              s = 100 === t;
            return (
              (0, o.useEffect)(() => {
                s && r && r();
              }, [s, r]),
              i().createElement(Qn, {
                size: e,
                disabled: n,
                baseStyles: a,
                isComplete: s,
                lineRef: u,
              })
            );
          };
        let er, tr;
        (!(function (e) {
          ((e.Idle = "Idle"), (e.Grow = "Grow"), (e.Shrink = "Shrink"), (e.End = "End"));
        })(er || (er = {})),
          (function (e) {
            ((e.Idle = "Idle"), (e.In = "In"), (e.End = "End"));
          })(tr || (tr = {})));
        const ur = "ProgressBarDeltaSimple_base_6c",
          nr = "ProgressBarDeltaSimple_delta_99",
          rr = (0, o.memo)(
            ({
              transitionDuration: e,
              transitionDelay: t,
              freezed: u,
              from: n,
              size: r,
              to: a,
              onEndAnimation: s,
              onChangeAnimationState: l,
            }) => {
              const c = a < n,
                d = (0, o.useState)(tr.Idle),
                m = d[0],
                E = d[1],
                _ = m === tr.In,
                g = m === tr.End,
                A = m === tr.Idle,
                h = (0, o.useCallback)(
                  (e) => {
                    (E(e), l && l(e));
                  },
                  [l],
                );
              ((0, o.useEffect)(() => {
                if (A && !u) {
                  return D(() => {
                    h(tr.In);
                  }, t);
                }
              }, [h, u, A, t]),
                (0, o.useEffect)(() => {
                  if (_) {
                    return D(() => {
                      (s && s(), h(tr.End));
                    }, e + t);
                  }
                }, [h, _, s, t, e]));
              const p = (0, o.useMemo)(
                  () => ({
                    width: "100%",
                    transitionDuration: `${e}ms`,
                    transitionDelay: `${t}ms`,
                    [c ? "left" : "right"]: "0",
                  }),
                  [c, t, e],
                ),
                F = (0, o.useMemo)(
                  () => ({
                    width: "0%",
                    transitionDuration: `${e}ms`,
                    transitionDelay: `${t}ms`,
                    [c ? "left" : "right"]: "0",
                  }),
                  [c, t, e],
                ),
                b = (0, o.useMemo)(
                  () => ({ width: `${Math.abs(n - a)}%`, left: `${c ? a : n}%` }),
                  [n, c, a],
                );
              return g
                ? null
                : i().createElement(
                    "div",
                    { className: ur, style: b },
                    i().createElement(
                      "div",
                      { style: A ? p : F, className: nr },
                      i().createElement(qn, { size: r }),
                    ),
                  );
            },
          ),
          ar = (0, o.memo)(
            ({
              to: e,
              size: t,
              from: u,
              lineRef: n,
              disabled: r,
              isComplete: a,
              animationSettings: s,
              onChangeAnimationState: l,
              onEndAnimation: c,
            }) => {
              const d = (0, o.useMemo)(
                () => ({
                  width: `${e}%`,
                  transitionDuration: `${s.line.duration}ms`,
                  transitionDelay: `${s.line.delay}ms`,
                }),
                [s.line.delay, s.line.duration, e],
              );
              return i().createElement(
                i().Fragment,
                null,
                i().createElement(Qn, {
                  size: t,
                  lineRef: n,
                  disabled: r,
                  isComplete: a,
                  baseStyles: d,
                }),
                u >= 0 &&
                  i().createElement(rr, {
                    transitionDuration: s.delta.duration,
                    transitionDelay: s.delta.delay,
                    freezed: s.freezed,
                    from: u,
                    size: t,
                    to: e,
                    onChangeAnimationState: l,
                    onEndAnimation: c,
                  }),
              );
            },
          ),
          or = "ProgressBarDeltaGrow_base_7e",
          ir = "ProgressBarDeltaGrow_base__withoutBounce_b5",
          sr = "ProgressBarDeltaGrow_glow_68",
          lr = (e) => (e ? { left: 0 } : { right: 0 }),
          cr = (e, t) => (e ? { right: 100 - t + "%" } : { left: `${t}%` }),
          dr = (e) => ({ transitionDuration: `${e}ms` }),
          mr = (0, o.memo)(
            ({
              transitionDuration: e,
              transitionDelay: t,
              freezed: u,
              from: n,
              size: a,
              to: s,
              onEndAnimation: l,
              onChangeAnimationState: c,
              className: d,
            }) => {
              const m = s < n,
                E = (0, o.useState)(er.Idle),
                _ = E[0],
                g = E[1],
                A = _ === er.End,
                h = _ === er.Idle,
                p = _ === er.Grow,
                F = _ === er.Shrink,
                b = (0, o.useCallback)(
                  (e) => {
                    (g(e), c && c(e));
                  },
                  [c],
                ),
                v = (0, o.useCallback)(
                  (e, t) =>
                    D(() => {
                      b(e);
                    }, t),
                  [b],
                );
              (0, o.useEffect)(() => {
                if (!u)
                  return h
                    ? v(er.Grow, t)
                    : p
                      ? v(er.Shrink, e)
                      : F
                        ? v(er.End, e)
                        : void (A && l && l());
              }, [v, u, A, p, h, F, l, t, e]);
              const C = (0, o.useMemo)(
                  () => Object.assign({ width: "100%" }, dr(e), lr(m)),
                  [m, e],
                ),
                f = (0, o.useMemo)(() => Object.assign({ width: "0%" }, dr(e), lr(m)), [m, e]),
                B = (0, o.useMemo)(
                  () => Object.assign({ width: "0%" }, cr(m, n), dr(e)),
                  [n, m, e],
                ),
                w = (0, o.useMemo)(
                  () => Object.assign({ width: `${Math.abs(s - n)}%` }, cr(m, n), dr(e)),
                  [n, m, s, e],
                );
              if (A) return null;
              const y = r()(or, d, m && 0 === s && ir);
              return i().createElement(
                "div",
                { style: h ? B : w, className: y },
                i().createElement(
                  "div",
                  { style: F ? f : C, className: sr },
                  i().createElement(qn, { size: a }),
                ),
              );
            },
          ),
          Er = (0, o.memo)(
            ({
              to: e,
              size: t,
              from: u,
              lineRef: n,
              disabled: r,
              isComplete: a,
              animationSettings: s,
              onEndAnimation: l,
              onChangeAnimationState: c,
            }) => {
              const d = e < u,
                m = (0, o.useState)(!1),
                E = m[0],
                _ = m[1],
                g = (0, o.useCallback)(
                  (e) => {
                    (e === er.Shrink && _(!0), c && c(e));
                  },
                  [c],
                ),
                A = (0, o.useMemo)(() => ({ width: `${u}%`, transitionProperty: "none" }), [u]),
                h = (0, o.useMemo)(
                  () => ({ width: `${e}%`, transitionDuration: `${s.line.duration}ms` }),
                  [s.line.duration, e],
                );
              return i().createElement(
                i().Fragment,
                null,
                i().createElement(Qn, {
                  size: t,
                  lineRef: n,
                  disabled: r,
                  isComplete: a,
                  withoutBounce: d && 0 === e,
                  baseStyles: E ? h : A,
                }),
                u >= 0 &&
                  i().createElement(mr, {
                    transitionDuration: s.delta.duration,
                    transitionDelay: s.delta.delay,
                    onChangeAnimationState: g,
                    freezed: s.freezed,
                    onEndAnimation: l,
                    from: u,
                    size: t,
                    to: e,
                    className: s.delta.className,
                  }),
              );
            },
          ),
          _r = ["onComplete", "onEndAnimation"];
        function gr() {
          return (
            (gr =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            gr.apply(this, arguments)
          );
        }
        const Ar = (0, o.memo)((e) => {
            let t = e.onComplete,
              u = e.onEndAnimation,
              n = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  r = {},
                  a = Object.keys(e);
                for (n = 0; n < a.length; n++) ((u = a[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
                return r;
              })(e, _r);
            const r = (0, o.useState)(!1),
              a = r[0],
              s = r[1],
              l = (0, o.useCallback)(() => {
                const e = 100 === n.to;
                (e !== a && s(e), e && t && t(), u && u());
              }, [a, t, u, n.to]);
            switch (n.animationSettings.type) {
              case Un.Simple:
                return i().createElement(ar, gr({}, n, { onEndAnimation: l, isComplete: a }));
              case Un.Growing:
                return i().createElement(Er, gr({}, n, { onEndAnimation: l, isComplete: a }));
              default:
                return null;
            }
          }),
          hr = ["onEndAnimation"];
        function pr() {
          return (
            (pr =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            pr.apply(this, arguments)
          );
        }
        const Fr = (0, o.memo)((e) => {
          let t = e.onEndAnimation,
            u = (function (e, t) {
              if (null == e) return {};
              var u,
                n,
                r = {},
                a = Object.keys(e);
              for (n = 0; n < a.length; n++) ((u = a[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
              return r;
            })(e, hr);
          const n = (0, o.useRef)({}),
            r = (0, o.useCallback)(() => {
              ((n.current.from = void 0), t && t());
            }, [t]),
            a = "number" == typeof n.current.from ? n.current.from : u.from;
          return (
            (n.current.from = a),
            i().createElement(Ar, pr({}, u, { onEndAnimation: r, key: `${a}-${u.to}`, from: a }))
          );
        });
        function br() {
          return (
            (br =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            br.apply(this, arguments)
          );
        }
        const Dr = (0, o.memo)(
            ({
              size: e,
              value: t,
              lineRef: u,
              disabled: n,
              deltaFrom: r,
              animationSettings: a,
              onEndAnimation: o,
              onChangeAnimationState: s,
              onComplete: l,
            }) => {
              if (r === t)
                return i().createElement(Jn, {
                  key: `${r}-${t}`,
                  size: e,
                  value: t,
                  lineRef: u,
                  disabled: n,
                  onComplete: l,
                });
              const c = {
                from: r,
                to: t,
                size: e,
                lineRef: u,
                disabled: n,
                animationSettings: a,
                onComplete: l,
                onEndAnimation: o,
                onChangeAnimationState: s,
              };
              return a.withStack
                ? i().createElement(Fr, c)
                : i().createElement(Ar, br({ key: `${r}-${t}` }, c));
            },
          ),
          vr = (e) => ({
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
          Cr = (e, t, u) => (u < e ? e : u > t ? t : u),
          fr = (e, t, u) => {
            if ("number" == typeof u) {
              return (Cr(0, t, u) / t) * 100;
            }
            return e;
          },
          Br = {
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
          wr = {
            freezed: !1,
            withStack: !1,
            type: Un.Growing,
            delta: { duration: 500, delay: 0 },
            line: { duration: 500, delay: 0 },
          },
          yr = (0, o.memo)(
            ({
              maxValue: e = 100,
              theme: t = Br,
              size: u = zn.Default,
              animationSettings: n = wr,
              disabled: a = !1,
              withoutBackground: s = !1,
              progressBarBackgroundClassMix: l,
              value: c,
              deltaFrom: d,
              lineRef: m,
              onChangeAnimationState: E,
              onEndAnimation: _,
              onComplete: g,
            }) => {
              const A = ((e, t, u) =>
                (0, o.useMemo)(() => {
                  const n = (Cr(0, t, e) / t) * 100;
                  return { value: n, deltaFrom: fr(n, t, u) };
                }, [u, t, e]))(c, e, d);
              return i().createElement(
                "div",
                { className: r()($n.base, $n[`base__${u}`]), style: vr(t) },
                !s && i().createElement(Kn, { size: u, classMix: l }),
                i().createElement(Dr, {
                  size: u,
                  lineRef: m,
                  disabled: a,
                  value: A.value,
                  deltaFrom: A.deltaFrom,
                  animationSettings: n,
                  onEndAnimation: _,
                  onChangeAnimationState: E,
                  onComplete: g,
                }),
              );
            },
          ),
          Sr = R.strings.dogtags.customization,
          kr = (0, o.memo)(
            ({
              id: e,
              infoTitle: t,
              infoText: u,
              isLocked: n,
              currentGrade: a,
              currentProgress: s,
              currentGradeValue: l,
              nextGradeValue: c,
              unlockText: d,
              progressNumberType: m,
              isExternalUnlockOnly: E,
            }) => {
              const _ = a + 1,
                g = (0, o.useMemo)(() => ({ componentId: e }), [e]),
                A = E && !n;
              return i().createElement(
                "div",
                { className: _u },
                i().createElement("div", { className: gu }, t),
                i().createElement("div", { className: wu }, u),
                n &&
                  i().createElement(
                    i().Fragment,
                    null,
                    i().createElement("div", { className: Iu }),
                    i().createElement(
                      "div",
                      { className: Pu },
                      i().createElement("div", { className: Hu }),
                      d,
                    ),
                  ),
                i().createElement(
                  Re,
                  {
                    contentId: R.views.lobby.dog_tags.DedicationTooltip("resId"),
                    isEnabled: !n,
                    args: g,
                  },
                  i().createElement(
                    "div",
                    null,
                    (!E || A) &&
                      i().createElement(
                        "div",
                        { className: bu },
                        i().createElement("div", { className: vu }, ne(s)),
                        _ < W &&
                          i().createElement(
                            i().Fragment,
                            null,
                            i().createElement("div", { className: fu }, "/"),
                            i().createElement("div", { className: Cu }, ne(n ? l : c, m)),
                          ),
                      ),
                    !n &&
                      i().createElement(
                        "div",
                        { className: Au },
                        i().createElement(yr, {
                          size: zn.Big,
                          value: s - l,
                          maxValue: c - l,
                          animationSettings: wr,
                        }),
                      ),
                    i().createElement(
                      "div",
                      { className: r()(Fu, n && Du) },
                      !n &&
                        i().createElement("div", { className: hu }, `${Sr.currentLevel()} ${G[a]}`),
                      !n && _ < W && i().createElement("div", { className: pu }, G[a + 1]),
                      !n && _ === W && i().createElement("div", { className: pu }),
                    ),
                  ),
                ),
              );
            },
          ),
          xr = (0, o.memo)(
            ({
              id: e,
              isLocked: t,
              infoTitle: u,
              infoText: n,
              currentGrade: a,
              currentProgress: s,
              nextGradeValue: l,
              unlockText: c,
              isDemoted: d,
              progressNumberType: m,
            }) => {
              const E = R.images.gui.maps.icons.dogtags,
                _ = a + 1,
                g = a + 2,
                A = E.level_shields[`Level_${_}`](),
                h = (0, o.useMemo)(() => ({ backgroundImage: `url(${A})` }), [A]),
                p = E.level_shields[`Level_gr_${g <= W ? g : 1}`](),
                F = (0, o.useMemo)(() => ({ backgroundImage: `url(${p})` }), [p]),
                b = t || d,
                D = r()(Su, _ === W && ku),
                v = (0, o.useMemo)(() => ({ componentId: e }), [e]);
              return i().createElement(
                "div",
                { className: _u },
                i().createElement("div", { className: gu }, u),
                i().createElement("div", { className: wu }, n),
                !b &&
                  i().createElement(
                    Re,
                    {
                      contentId: R.views.lobby.dog_tags.ThreeMonthsTooltip("resId"),
                      isEnabled: !0,
                      args: v,
                    },
                    i().createElement(
                      "div",
                      { className: Wu },
                      i().createElement("div", { className: Yu }),
                      i().createElement(
                        "div",
                        { className: Xu },
                        R.strings.dogtags.customization.skill_info(),
                        i().createElement("div", { className: yu }),
                      ),
                      i().createElement("div", { className: ju }),
                    ),
                  ),
                b &&
                  i().createElement(
                    i().Fragment,
                    null,
                    i().createElement("div", { className: Iu }),
                    i().createElement(
                      "div",
                      { className: Pu },
                      i().createElement("div", { className: Hu }),
                      c,
                    ),
                  ),
                !b &&
                  i().createElement(
                    Re,
                    {
                      contentId: R.views.lobby.dog_tags.DedicationTooltip("resId"),
                      isEnabled: !0,
                      args: v,
                    },
                    i().createElement(
                      "div",
                      { className: D },
                      i().createElement(
                        "div",
                        { className: xu },
                        i().createElement("div", { className: Tu, style: h }),
                        i().createElement("div", { className: Nu }, ne(s, m)),
                      ),
                      _ < W &&
                        i().createElement(
                          i().Fragment,
                          null,
                          i().createElement("div", { className: Mu }),
                          i().createElement(
                            "div",
                            { className: Lu },
                            i().createElement("div", { className: Ou, style: F }),
                            i().createElement("div", { className: Ru }, ne(l, m)),
                          ),
                        ),
                    ),
                  ),
              );
            },
          ),
          Lr = R.images.gui.maps.icons.dogtags,
          Tr = (0, o.memo)(
            ({
              id: e,
              isLocked: t,
              infoTitle: u,
              infoText: n,
              currentGrade: a,
              currentProgress: s,
              nextGradeValue: l,
              unlockText: c,
              progressNumberType: d,
            }) => {
              const m = a + 1,
                E = a + 2,
                _ = Lr.level_shields[`Level_${m}`](),
                g = (0, o.useMemo)(() => ({ backgroundImage: `url(${_})` }), [_]),
                A = E < W ? Lr.level_shields[`Level_gr_${E}`]() : "",
                h = (0, o.useMemo)(() => ({ backgroundImage: `url(${A})` }), [A]),
                p = r()(Su, { [ku]: 4 === a }),
                F = (0, o.useMemo)(() => ({ componentId: e }), [e]);
              return i().createElement(
                "div",
                { className: _u },
                i().createElement("div", { className: gu }, u),
                i().createElement("div", { className: wu }, n),
                t &&
                  i().createElement(
                    i().Fragment,
                    null,
                    i().createElement("div", { className: Iu }),
                    i().createElement(
                      "div",
                      { className: Pu },
                      i().createElement("div", { className: Hu }),
                      c,
                    ),
                  ),
                !t &&
                  i().createElement(
                    Re,
                    {
                      contentId: R.views.lobby.dog_tags.TriumphTooltip("resId"),
                      isEnabled: !0,
                      args: F,
                    },
                    i().createElement(
                      "div",
                      { className: p },
                      i().createElement(
                        "div",
                        { className: xu },
                        i().createElement("div", { className: Tu, style: g }),
                        i().createElement("div", { className: Nu }, ne(s, d)),
                      ),
                      m < 4 && i().createElement("div", { className: Mu }),
                      m < 4 &&
                        i().createElement(
                          "div",
                          { className: Lu },
                          i().createElement("div", { className: Ou, style: h }),
                          i().createElement("div", { className: Ru }, ne(l, d)),
                        ),
                    ),
                  ),
              );
            },
          ),
          Nr = R.images.gui.maps.icons.dogtags,
          Rr = (0, o.memo)(
            ({
              id: e,
              isLocked: t,
              infoTitle: u,
              infoText: n,
              currentGrade: a,
              currentProgress: s,
              nextGradeValue: l,
              unlockText: c,
              isDemoted: d,
              progressNumberType: m,
            }) => {
              const E = a + 1,
                _ = a + 2,
                g = Nr.level_shields[`Level_${E}`](),
                A = (0, o.useMemo)(() => ({ backgroundImage: `url(${g})` }), [g]),
                h = Nr.level_shields[`Level_gr_${_ <= W ? _ : 1}`](),
                p = (0, o.useMemo)(() => ({ backgroundImage: `url(${h})` }), [h]),
                F = t || d,
                b = r()(Su, E === W && ku),
                D = (0, o.useMemo)(() => ({ componentId: e }), [e]),
                v = E < W;
              return i().createElement(
                "div",
                { className: _u },
                i().createElement("div", { className: gu }, u),
                i().createElement("div", { className: wu }, n),
                !F &&
                  i().createElement(
                    Re,
                    {
                      contentId: R.views.lobby.dog_tags.RankedEfficiencyTooltip("resId"),
                      isEnabled: !0,
                      args: D,
                    },
                    i().createElement(
                      "div",
                      { className: Wu },
                      i().createElement("div", { className: Yu }),
                      i().createElement(
                        "div",
                        { className: Xu },
                        R.strings.dogtags.customization.ranked_skill_info(),
                        i().createElement("div", { className: yu }),
                      ),
                      i().createElement("div", { className: ju }),
                    ),
                  ),
                F &&
                  i().createElement(
                    i().Fragment,
                    null,
                    i().createElement("div", { className: Iu }),
                    i().createElement(
                      "div",
                      { className: Pu },
                      i().createElement("div", { className: Hu }),
                      c,
                    ),
                  ),
                !F &&
                  i().createElement(
                    Re,
                    {
                      contentId: R.views.lobby.dog_tags.DedicationTooltip("resId"),
                      isEnabled: !0,
                      args: D,
                    },
                    i().createElement(
                      "div",
                      { className: b },
                      i().createElement(
                        "div",
                        { className: xu },
                        i().createElement("div", { className: Tu, style: A }),
                        i().createElement("div", { className: Nu }, ne(s, m)),
                      ),
                      v &&
                        i().createElement(
                          i().Fragment,
                          null,
                          i().createElement("div", { className: Mu }),
                          i().createElement(
                            "div",
                            { className: Lu },
                            i().createElement("div", { className: Ou, style: p }),
                            i().createElement("div", { className: Ru }, ne(l, m)),
                          ),
                        ),
                    ),
                  ),
              );
            },
          ),
          Mr = (0, o.memo)(
            ({
              infoTitle: e,
              infoText: t,
              isLocked: u,
              unlockText: n,
              currentProgress: r,
              skipProgressInDescr: a,
            }) =>
              i().createElement(
                "div",
                { className: _u },
                i().createElement(jn, { className: gu, text: e }),
                i().createElement(jn, { className: Bu, text: t }),
                !a && i().createElement(jn, { className: Gu, text: ne(r) }),
                u &&
                  i().createElement(
                    i().Fragment,
                    null,
                    i().createElement("div", { className: Iu }),
                    i().createElement(
                      "div",
                      { className: Pu },
                      i().createElement("div", { className: Hu }),
                      i().createElement(jn, { text: n }),
                    ),
                  ),
              ),
          );
        function Or() {
          return (
            (Or =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            Or.apply(this, arguments)
          );
        }
        const Ir = ({ currentItem: e }) => {
          const t = e.id,
            u = e.purpose,
            n = e.currentGrade,
            r = e.type,
            a = e.currentGradeValue,
            o = e.currentProgress,
            s = q(t, r, u, n).strings;
          if (!s) return (console.warn(`Component ${t} is missing translation info.`), null);
          const l = s.description_locked(),
            c = s.title(),
            d = s.description(),
            m = l.replace("{unlock_value}", String(ne(a))),
            E = {
              [I.Dedication]: kr,
              [I.Skill]: xr,
              [I.RankedSkill]: Rr,
              [I.Triumph]: Tr,
              [I.Medal]: Gn,
              [I.Base]: Gn,
              [I.Static]: Mr,
            },
            _ = { infoTitle: c, infoText: d, unlockText: m, currentProgress: o },
            g = E[u];
          return g
            ? i().createElement(g, Or({}, e, _))
            : (console.warn(
                `Invalid component purpose ${u}. Available component purposes ${Object.keys(E).join(", ")}.`,
              ),
              null);
        };
        var Pr = u(664);
        const Hr = "Dogtags_base_46",
          Wr = "Dogtags_dogtags_top_26",
          Xr = "Dogtags_dogtags_bottom_3d",
          Yr = "Dogtags_background_f8",
          jr = "Dogtags_playerInfoShadow_a4",
          Gr = "Dogtags_name_95",
          $r = "Dogtags_clan_a3",
          zr = "Dogtags_engraving_b0",
          Ur = "Dogtags_shadow_8c",
          Kr = "Dogtags_trackerInfoWrapper_fd",
          Vr = "Dogtags_trackerText_a4",
          qr = "Dogtags_trackerValue_f5",
          Zr = "Dogtags_trackerDigit_c0",
          Qr = "Dogtags_spaceDigit_86",
          Jr = "Dogtags_flameAnimation_a9",
          ea = "Dogtags_flameAnimation__appear_2a",
          ta = "Dogtags_flameAnimation__appearActive_b3",
          ua = "Dogtags_flameAnimation__appearDone_cb",
          na = "Dogtags_flameAnimation__enter_a3",
          ra = "Dogtags_flameAnimation__enterActive_53",
          aa = "Dogtags_flameAnimation__enterDone_b7",
          oa = "Dogtags_flameAnimation__exit_20",
          ia = "Dogtags_flameAnimation__exitActive_0e",
          sa = "Dogtags_flameAnimation__exitDone_df",
          la = "Flame_base_90",
          ca = "Flame_slides_58",
          da = "Flame_frame_29",
          ma = (0, o.memo)(({ className: e }) => {
            const t = (() => {
              const e = R.images.gui.maps.icons.dogtags.icons.flame;
              return Array(42)
                .fill(null)
                .map((t, u) => {
                  const n = `flame_${`0${u}`.slice(-2)}`;
                  return n in e ? e[n]() : e.flame_00();
                });
            })();
            return i().createElement(
              "div",
              { className: r()(la, e), "data-testid": "Flame" },
              i().createElement(
                "div",
                { className: ca },
                t.map((e) => i().createElement("img", { key: e, src: e, className: da })),
              ),
            );
          }),
          Ea = R.images.gui.maps.icons.dogtags.big.digits;
        Object.keys(Object.getPrototypeOf(Ea))
          .filter((e) => "$" !== e[0])
          .map((e) => Ea[e]())
          .map((e) => {
            new Image().src = e;
          });
        const _a = (e) => {
            const t = e.currentTarget.width / e.currentTarget.height;
            ((e.currentTarget.style.width = 16 * t + "%"),
              (e.currentTarget.style.display = "flex"));
          },
          ga = {
            appear: ea,
            appearActive: ta,
            appearDone: ua,
            enter: na,
            enterActive: ra,
            enterDone: aa,
            exit: oa,
            exitActive: ia,
            exitDone: sa,
          },
          Aa = ({ playerName: e, clanTag: t, background: u, engraving: n, isHighlighted: r }) => {
            const s = u.currentGrade,
              l = n.currentGrade,
              c = q(u.id, O.Background, u.purpose || "default", s || 0, "big"),
              d = q(n.id, O.Engraving, n.purpose || "dedication", l || 0, "big"),
              m = n.displayableProgress.split(/\[|\]/).reduce((e, t, u) => {
                const n = u % 2 == 1;
                return (e.push(...(n ? [t] : t.split(""))), e);
              }, []);
            const E = d.strings ? d.strings.title() : null,
              _ = ce(c.image),
              g = ce(d.image),
              A = ((e) => {
                const t = (0, o.useRef)(!1);
                return (
                  (0, o.useEffect)(() => {
                    t.current = e;
                  }),
                  t.current
                );
              })(r);
            return (
              (0, o.useEffect)(() => {
                r && !A ? a(R.sounds.dt_flame_start()) : A && !r && a(R.sounds.dt_flame_stop());
              }, [r, A]),
              i().createElement(
                "div",
                { className: Hr },
                i().createElement(
                  Pr.Z,
                  {
                    in: r,
                    timeout: 400,
                    className: Jr,
                    classNames: ga,
                    mountOnEnter: !0,
                    unmountOnExit: !0,
                    appear: !0,
                  },
                  i().createElement(ma, null),
                ),
                i().createElement(
                  "div",
                  { className: Wr },
                  i().createElement("div", { className: Yr, style: _ }),
                  i().createElement("div", { className: Ur }),
                  i().createElement("div", { className: jr }),
                  i().createElement("div", { className: Gr }, e),
                  i().createElement("div", { className: $r }, t),
                  i().createElement("div", { className: zr, style: g }),
                ),
                i().createElement(
                  "div",
                  { className: Xr },
                  i().createElement(
                    "div",
                    { className: Kr },
                    i().createElement("div", { className: Vr }, E),
                    i().createElement(
                      "div",
                      { className: qr },
                      m.map((e, t) => {
                        if (" " === e)
                          return i().createElement("div", { key: e + t, className: Qr });
                        const u = le(e, Ea);
                        return i().createElement("img", {
                          key: `${u}-${t}`,
                          onLoad: _a,
                          className: Zr,
                          src: u,
                        });
                      }),
                    ),
                  ),
                ),
              )
            );
          },
          ha = "FilterBar_base_66",
          pa = "FilterBar_purposeGroups_85",
          Fa = "FilterBar_buttonWrapper_c2",
          ba = "FilterBar_buttonLabelSpacing_6c",
          Da = "FilterBar_bubbleWrapper_27",
          va = "FilterBar_availableItems_4d",
          Ca = "FilterBar_availableItemsCount_a1",
          fa = "FilterBar_newCount_c9",
          Ba = "ToggleButton_base_66",
          wa = "ToggleButton_content_2f",
          ya = "ToggleButton_overlay_49",
          Sa = "ToggleButton_base__active_c6",
          ka = "ToggleButton_indicator_c1",
          xa = ["active", "className", "children", "size"];
        function La() {
          return (
            (La =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            La.apply(this, arguments)
          );
        }
        const Ta = (0, o.memo)((e) => {
          let t = e.active,
            u = e.className,
            n = e.children,
            a = e.size,
            o = void 0 === a ? c.small : a,
            s = (function (e, t) {
              if (null == e) return {};
              var u,
                n,
                r = {},
                a = Object.keys(e);
              for (n = 0; n < a.length; n++) ((u = a[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
              return r;
            })(e, xa);
          const l = r()(Ba, u, t && Sa);
          return i().createElement(
            "div",
            { className: l },
            i().createElement(
              m,
              La({}, s, { type: "secondary", size: o }),
              i().createElement("span", { className: wa }, n),
            ),
            i().createElement("div", { className: ya }),
            i().createElement("div", { className: ka }),
          );
        });
        let Na;
        !(function (e) {
          ((e[(e.LEFT = 0)] = "LEFT"),
            (e[(e.WHEEL = 1)] = "WHEEL"),
            (e[(e.RIGHT = 2)] = "RIGHT"),
            (e[(e.FOURTH = 3)] = "FOURTH"),
            (e[(e.FIFTH = 4)] = "FIFTH"));
        })(Na || (Na = {}));
        const Ra = {
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
        let Ma, Oa, Ia;
        (!(function (e) {
          ((e.small = "small"),
            (e.medium = "medium"),
            (e.large = "large"),
            (e.extraLarge = "extraLarge"));
        })(Ma || (Ma = {})),
          (function (e) {
            ((e.primary = "primary"), (e.main = "main"));
          })(Oa || (Oa = {})),
          (function (e) {
            ((e.Center = "center"), (e.Bottom = "bottom"));
          })(Ia || (Ia = {})));
        const Pa = [
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
        function Ha() {
          return (
            (Ha =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            Ha.apply(this, arguments)
          );
        }
        const Wa = (e) => {
            let t = e.id,
              u = e.isChecked,
              n = void 0 !== u && u,
              s = e.isDisabled,
              l = void 0 !== s && s,
              c = e.isAlert,
              d = void 0 !== c && c,
              m = e.size,
              E = void 0 === m ? Ma.medium : m,
              _ = e.type,
              g = void 0 === _ ? Oa.primary : _,
              A = e.soundHover,
              h = void 0 === A ? "highlight" : A,
              p = e.soundClick,
              F = void 0 === p ? "play" : p,
              b = e.onMouseEnter,
              D = e.onMouseLeave,
              v = e.onMouseUp,
              C = e.onMouseDown,
              f = e.onClick,
              B = e.onChange,
              w = e.onFocus,
              y = e.onBlur,
              S = e.text,
              k = e.contentStyles,
              x = e.children,
              L = e.alignment,
              T = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  r = {},
                  a = Object.keys(e);
                for (n = 0; n < a.length; n++) ((u = a[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
                return r;
              })(e, Pa);
            const N = (0, o.useState)(!1),
              R = N[0],
              M = N[1],
              O = (0, o.useState)(!1),
              I = (O[0], O[1]),
              P = (0, o.useCallback)(
                (e) => {
                  l || (B && B(), f && f(e));
                },
                [l, B, f],
              ),
              H = (0, o.useCallback)(
                (e) => {
                  const t = e.button === Na.LEFT;
                  l || (t && M(!0), t && C && C(e), F && a(F));
                },
                [l, C, F],
              ),
              W = (0, o.useCallback)(
                (e) => {
                  l || (M(!1), v && v(e));
                },
                [l, v],
              ),
              X = (0, o.useCallback)(
                (e) => {
                  l || (b && b(e), h && a(h));
                },
                [l, b, h],
              ),
              Y = (0, o.useCallback)(
                (e) => {
                  l || (M(!1), D && D(e));
                },
                [l, D],
              ),
              j = (0, o.useCallback)(
                (e) => {
                  l || (I(!0), w && w(e));
                },
                [l, w],
              ),
              G = (0, o.useCallback)(
                (e) => {
                  l || (I(!1), y && y(e));
                },
                [l, y],
              ),
              $ = i().createElement(
                "div",
                { className: Ra.label },
                i().createElement(
                  "div",
                  { className: r()(Ra.labelContent, "s-labelContent"), style: k },
                  S || x,
                ),
              );
            return i().createElement(
              "div",
              Ha(
                {
                  id: t,
                  className: r()(Ra.base, Ra[`base__${E}`], Ra[`base__${g}`], {
                    [Ra.base__checked]: n,
                    [Ra.base__disabled]: l,
                    [Ra.base__mouseDown]: R,
                    [Ra.base__alert]: d,
                    [Ra.base__center]: L === Ia.Center,
                    [Ra.base__bottom]: L === Ia.Bottom,
                  }),
                  onClick: P,
                  onMouseEnter: X,
                  onMouseLeave: Y,
                  onMouseDown: H,
                  onMouseUp: W,
                  onFocus: j,
                  onBlur: G,
                },
                T,
              ),
              i().createElement(
                "div",
                { className: Ra.input },
                i().createElement("div", { className: Ra.alertOverlay }),
                i().createElement("div", { className: Ra.inputHoverOverlay }),
                i().createElement("div", { className: Ra.highlight }),
              ),
              i().createElement("div", { className: Ra.checkmark }),
              ((S || x) && $) || null,
            );
          },
          Xa = R.strings.dogtags.component.purposeGroup,
          Ya = (0, o.memo)(
            ({
              availablePurposeGroups: e,
              purposeGroupFilters: t,
              setPurposeGroupFilters: u,
              showOnlyAvailableItems: n,
              setShowOnlyAvailableItems: r,
              availableItemsCount: a,
              newEngravingSkillCount: s = 0,
              newEngravingDedicationCount: l = 0,
              newEngravingTriumphCount: c = 0,
              newEngravingStaticCount: d = 0,
            }) => {
              const m = (0, o.useCallback)(
                  (e) => () => {
                    u((t) => Object.assign({}, t, { [e]: !t[e] }));
                  },
                  [u],
                ),
                E = (0, o.useCallback)(() => r((e) => !e), [r]),
                _ = { [P.Dedication]: l, [P.Triumph]: c, [P.Season]: s, [P.Static]: d };
              return i().createElement(
                "div",
                { className: ha },
                e.length > 0 &&
                  i().createElement(
                    "div",
                    { className: pa },
                    e.map((e) => {
                      const u = t[e],
                        n = e in Xa ? Xa[e]() : Xa.dedication(),
                        r = _[e] || 0;
                      return i().createElement(
                        "div",
                        { className: Fa, key: e },
                        i().createElement(
                          Ta,
                          { active: u, onClick: m(e) },
                          i().createElement("span", { className: ba }, n),
                        ),
                        r > 0 &&
                          i().createElement(
                            "div",
                            { className: Da },
                            i().createElement(
                              "div",
                              { className: fa },
                              i().createElement(ie, { value: r }),
                            ),
                          ),
                      );
                    }),
                  ),
                i().createElement(
                  "div",
                  { className: va },
                  i().createElement(Wa, {
                    isChecked: n,
                    size: "medium",
                    text: R.strings.dogtags.customization.showAvailable(),
                    type: "main",
                    soundHover: "highlight",
                    soundClick: "play",
                    onChange: E,
                  }),
                  i().createElement("span", { className: Ca }, a),
                ),
              );
            },
          ),
          ja = "NoResults_base_35",
          Ga = "NoResults_message_41",
          $a = "NoResults_message_icon_a4",
          za = ({ className: e, clearFilters: t }) => {
            const u = r()(ja, e);
            return i().createElement(
              "div",
              { className: u },
              i().createElement(
                "p",
                { className: Ga },
                i().createElement("img", {
                  src: R.images.gui.maps.icons.dogtags.icons.alert(),
                  className: $a,
                }),
                R.strings.dogtags.customization.filter.noResults(),
              ),
              i().createElement(
                m,
                { type: "secondary", size: c.medium, onClick: t },
                R.strings.dogtags.customization.filter.restoreFilter(),
              ),
            );
          },
          Ua = "Customization_base_4e",
          Ka = "Customization_checkIcon_bf",
          Va = "Customization_allEquipped_ed",
          qa = "Customization_alertMessage_c4",
          Za = "Customization_alertIcon_ce",
          Qa = "Customization_selectionWrapper_e5",
          Ja = "Customization_selection_6b",
          eo = "Customization_resetBtn_f7",
          to = R.strings.dogtags.customization.allApplied(),
          uo = R.strings.dogtags.customization.selectedNotAvailable(),
          no = R.strings.dogtags.customization.deprecated(),
          ro = R.strings.dogtags.customization.pills.engraving(),
          ao = R.strings.dogtags.customization.pills.background(),
          oo = (0, o.memo)(({ selectedItems: e, equippedItems: t, onItemReset: u }) => {
            const n = e.engraving.id === t.engraving.id,
              r = e.background.id === t.background.id,
              s = e.engraving.isLocked,
              l = e.background.isLocked;
            function c(e) {
              return () => {
                (a(R.sounds.dt_locked_reset_button()), u(e));
              };
            }
            const d = (0, o.useCallback)(() => {
                a(R.sounds.highlight());
              }, []),
              m = [];
            return (
              ((!r && l) || (!n && s)) && m.push(uo),
              (e.engraving.isDeprecated || e.background.isDeprecated) && m.push(no),
              i().createElement(
                "div",
                { className: Ua },
                0 === m.length &&
                  r &&
                  n &&
                  i().createElement(
                    "div",
                    { className: Va },
                    i().createElement("div", { className: Ka }),
                    to,
                  ),
                m.length > 0 &&
                  i().createElement(
                    "div",
                    { className: qa },
                    i().createElement("div", { className: Za }),
                    m.map((e) => i().createElement("div", { key: e }, e)),
                  ),
                (!r || !n) &&
                  i().createElement(
                    "div",
                    { className: Qa },
                    !r &&
                      i().createElement(
                        "div",
                        { className: Ja, onClick: c(O.Background), onMouseEnter: d },
                        ao,
                        i().createElement("div", { className: eo }),
                      ),
                    !n &&
                      i().createElement(
                        "div",
                        { className: Ja, onClick: c(O.Engraving), onMouseEnter: d },
                        ro,
                        i().createElement("div", { className: eo }),
                      ),
                  ),
              )
            );
          }),
          io = "Onboarding_base_f8",
          so = "Onboarding_header_f2",
          lo = "Onboarding_center_47",
          co = "Onboarding_closeBtn_1a",
          mo = "Onboarding_body_31",
          Eo = "Onboarding_overlayReveal_e3",
          _o = "Onboarding_overlay_02",
          go = "Onboarding_playBtnWrapper_1d",
          Ao = "Onboarding_playBtn_22",
          ho = "Onboarding_footer_64",
          po = "Onboarding_pagination_e5",
          Fo = "Onboarding_paginationBtn_8d",
          bo = "Onboarding_selected_d7",
          Do = "Onboarding_replay_81",
          vo = "Onboarding_replayIcon_9b",
          Co = "Onboarding_overlayInnerWrapper_df",
          fo = "Onboarding_overlayTitle_96",
          Bo = "Onboarding_overlayText_c2",
          wo = {
            slideOut: "Reveal_slideOut_ec",
            slideIn: "Reveal_slideIn_00",
            slideLeftOut: "Reveal_slideLeftOut_84",
            slideLeftIn: "Reveal_slideLeftIn_92",
            slideRightOut: "Reveal_slideRightOut_8b",
            slideRightIn: "Reveal_slideRightIn_4d",
            fadeOut: "Reveal_fadeOut_d6",
            fadeIn: "Reveal_fadeIn_38",
            bg_fadeOut: "Reveal_bg_fadeOut_f3",
            fadeOutBlur: "Reveal_fadeOutBlur_3f",
            bg_fadeIn: "Reveal_bg_fadeIn_a4",
            fadeInBlur: "Reveal_fadeInBlur_57",
            fadeDownIn: "Reveal_fadeDownIn_bc",
            fadeInUp: "Reveal_fadeInUp_1d",
            fadeDownOut: "Reveal_fadeDownOut_f6",
            fadeInDown: "Reveal_fadeInDown_7e",
          },
          yo = (0, o.memo)(
            ({
              children: e,
              type: t = "slide",
              duration: u = 200,
              className: n,
              isOut: a = !1,
              delayIn: s = "0ms",
              delayOut: l = "0ms",
              isDisabled: c = !1,
              onAnimationComplete: d,
            }) => {
              const m = (0, o.useMemo)(
                  () => ({ animationDelay: a ? l : s, animationDuration: `${u}ms` }),
                  [a, s, l, u],
                ),
                E = r()(wo[`${t}${a ? "Out" : "In"}`], n);
              return c
                ? i().createElement("div", { className: n }, e)
                : i().createElement("div", { onAnimationEnd: d, className: E, style: m }, e);
            },
          );
        var So;
        !(function (e) {
          ((e[(e.First = 0)] = "First"), (e[(e.Second = 1)] = "Second"));
        })(So || (So = {}));
        const ko = R.strings.dogtags.onboarding.header.title(),
          xo = R.strings.dogtags.onboarding.header.close(),
          Lo = R.strings.dogtags.onboarding.overlay.pagination.first(),
          To = R.strings.dogtags.onboarding.overlay.pagination.second(),
          No = R.strings.dogtags.onboarding.overlay.replay(),
          Ro = (0, o.memo)(({ onClose: e }) => {
            const t = T("model", L.None).onPlayVideo,
              u = (0, o.useState)(!1),
              n = u[0],
              s = u[1],
              l = (0, o.useState)(!1),
              c = l[0],
              d = l[1],
              E = (0, o.useState)(So.First),
              _ = E[0],
              g = E[1],
              A = (e) => () => (a(R.sounds.play()), g(e)),
              h = (0, o.useCallback)((t) => (_ === So.First ? g(So.Second) : e(t)), [_, e]),
              p = (0, o.useCallback)(
                () => (
                  a(R.sounds.play()),
                  _ === So.First
                    ? (setTimeout(() => s(!0), 500), t({ urlKey: "onboardingVideo1" }))
                    : (setTimeout(() => d(!0), 500), t({ urlKey: "onboardingVideo2" }))
                ),
                [_, t],
              ),
              F = (0, o.useCallback)(() => a(R.sounds.highlight()), []),
              D = ((v = n),
              (C = c),
              {
                [So.First]: {
                  title: v
                    ? R.strings.dogtags.onboarding.overlay.first.postVideo.title()
                    : R.strings.dogtags.onboarding.overlay.first.preVideo.title(),
                  text: v
                    ? R.strings.dogtags.onboarding.overlay.first.postVideo.text()
                    : R.strings.dogtags.onboarding.overlay.first.preVideo.text(),
                  button: R.strings.dogtags.onboarding.overlay.button.next(),
                  background: R.images.gui.maps.icons.dogtags.icons.onboarding_bg_1(),
                },
                [So.Second]: {
                  title: C
                    ? R.strings.dogtags.onboarding.overlay.second.postVideo.title()
                    : R.strings.dogtags.onboarding.overlay.second.preVideo.title(),
                  text: C
                    ? R.strings.dogtags.onboarding.overlay.second.postVideo.text()
                    : R.strings.dogtags.onboarding.overlay.second.preVideo.text(),
                  button: R.strings.dogtags.onboarding.overlay.button.affirmative(),
                  background: R.images.gui.maps.icons.dogtags.icons.onboarding_bg_2(),
                },
              })[_];
            var v, C;
            const f = ((e) => ({ backgroundImage: `url(${e.background})` }))(D),
              B = r()(Fo, _ === So.First && bo),
              w = r()(Fo, _ === So.Second && bo);
            return i().createElement(
              "div",
              { className: io },
              i().createElement(
                "div",
                { className: so },
                i().createElement("div", { className: lo }, ko),
                i().createElement(
                  "div",
                  { className: co },
                  i().createElement(b, {
                    caption: xo,
                    type: "close",
                    side: "right",
                    onClick: e,
                    onMouseEnter: F,
                  }),
                ),
              ),
              i().createElement(
                "div",
                { className: mo, style: f },
                i().createElement(
                  yo,
                  { type: "fade", className: Eo },
                  i().createElement(
                    "div",
                    { className: _o },
                    ((!n && _ === So.First) || (!c && _ === So.Second)) &&
                      i().createElement(
                        "div",
                        { className: go, onClick: p, onMouseEnter: F },
                        i().createElement("div", { className: Ao }),
                      ),
                    i().createElement(
                      "div",
                      { className: Co },
                      i().createElement("div", { className: fo }, D.title),
                      i().createElement("div", { className: Bo }, D.text),
                      ((_ === So.First && n) || (_ === So.Second && c)) &&
                        i().createElement(
                          m,
                          { type: "main", size: "medium", onClick: h, onMouseEnter: F },
                          D.button,
                        ),
                    ),
                  ),
                ),
              ),
              i().createElement(
                "div",
                { className: ho },
                ((_ === So.First && n) || (_ === So.Second && c)) &&
                  i().createElement(
                    "div",
                    { className: Do, onClick: p, onMouseEnter: F },
                    i().createElement("div", { className: vo }),
                    No,
                  ),
                i().createElement(
                  "div",
                  { className: po },
                  i().createElement(
                    "div",
                    { className: B, onClick: A(So.First), onMouseEnter: F },
                    Lo,
                  ),
                  i().createElement(
                    "div",
                    { className: w, onClick: A(So.Second), onMouseEnter: F },
                    To,
                  ),
                ),
              ),
            );
          }),
          Mo = "DogTagsApp_outerContainer_28",
          Oo = "DogTagsApp_outerContainer_topView_6d",
          Io = "DogTagsApp_base_c2",
          Po = "DogTagsApp_blur_30",
          Ho = "DogTagsApp_baseReveal_e4",
          Wo = "DogTagsApp_onboardingWrapper_b7",
          Xo = "DogTagsApp_infoScreenReveal_1a",
          Yo = "DogTagsApp_customizationWrapper_95",
          jo = "DogTagsApp_routerReveal_45",
          Go = "DogTagsApp_backBtnWrapper_85",
          $o = "DogTagsApp_closeBtnWrapper_69",
          zo = 300,
          Uo = () => {
            const e = T("model", L.None),
              t = e.onTabSelect,
              u = e.onboardingEnabled,
              n = e.onOnboardingCloseClick,
              a = e.onInfoButtonClick,
              s = e.isTopView,
              l = e.onExit,
              c = (0, o.useState)(!1),
              d = c[0],
              m = c[1],
              E = (0, o.useState)(null),
              _ = E[0],
              g = E[1],
              A = (0, o.useCallback)((e) => {
                const t = Number(e.currentTarget.getAttribute("tab-key"));
                g(t);
              }, []);
            (0, o.useEffect)(() => {
              if (null !== _)
                return D(() => {
                  (g(null), t({ newTab: _ }));
                }, zo);
            }, [_, t]);
            const h = (0, o.useState)(!1),
              p = h[0],
              F = h[1],
              v = (0, o.useState)(!1),
              C = v[0],
              f = v[1],
              B = (0, o.useState)(u),
              w = B[0],
              y = B[1],
              S = (0, o.useState)(!1),
              k = S[0],
              x = S[1],
              N = (0, o.useCallback)(() => {
                F(!0);
              }, []),
              M = (0, o.useCallback)(() => {
                f(!0);
              }, []),
              O = (0, o.useCallback)(() => {
                x(!0);
              }, []),
              I = (0, o.useCallback)(
                (e) => {
                  27 === (e.keyCode || e.which) && (d ? m(!1) : w ? x(!0) : f(!0));
                },
                [d, w],
              );
            (0, o.useEffect)(
              () => (
                window.addEventListener("keydown", I),
                () => window.removeEventListener("keydown", I)
              ),
              [I],
            );
            const P = (0, o.useCallback)(() => {
                C && l();
              }, [l, C]),
              H = (0, o.useCallback)(() => {
                p && (F(!1), a());
              }, [p, a]),
              W = (0, o.useCallback)(() => {
                k && (y(!1), n());
              }, [n, k]),
              X = R.strings.dogtags.customization.button.backDashboard_glow(),
              Y = R.strings.dogtags.customization.button.backDashboard_gray(),
              j = R.strings.dogtags.onboarding.header.close(),
              G = r()(Io, w && Po);
            return i().createElement(
              "div",
              { className: r()(Mo, s && Oo) },
              i().createElement(
                yo,
                { type: "fade", isOut: C, duration: zo, className: Ho, onAnimationComplete: P },
                i().createElement(
                  "div",
                  { className: G },
                  s &&
                    i().createElement(
                      "div",
                      { className: Go },
                      i().createElement(b, {
                        caption: X,
                        type: "back",
                        side: "left",
                        onClick: M,
                        goto: Y,
                      }),
                    ),
                  !s &&
                    i().createElement(
                      "div",
                      { className: $o },
                      i().createElement(b, {
                        caption: j,
                        type: "close",
                        side: "right",
                        onClick: M,
                      }),
                    ),
                  !d &&
                    i().createElement(
                      yo,
                      {
                        className: Xo,
                        type: "bg_fade",
                        isDisabled: C,
                        isOut: p,
                        duration: zo,
                        onAnimationComplete: H,
                      },
                      i().createElement(
                        "div",
                        { className: Yo },
                        i().createElement(Ot, { onTabClick: A, onInfoClick: N }),
                        i().createElement(
                          yo,
                          {
                            className: jo,
                            type: "slide",
                            isOut: null !== _,
                            isDisabled: p || C,
                            duration: zo,
                          },
                          i().createElement(Eu, null),
                        ),
                      ),
                    ),
                ),
              ),
              w &&
                i().createElement(
                  yo,
                  { type: "fade", isOut: k, className: Wo, duration: zo, onAnimationComplete: W },
                  i().createElement(Ro, { onClose: O }),
                ),
            );
          },
          Ko = document.createElement("div");
        ((window.onload = () => {
          (document.body.appendChild(Ko), document.body.setAttribute("style", "margin: 0;"));
        }),
          engine.whenReady.then(() => {
            A().render(i().createElement(_, null, i().createElement(Uo, null)), Ko);
          }));
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
        for (s = 0; s < deferred.length; s++) {
          for (var [t, u, n] = deferred[s], a = !0, o = 0; o < t.length; o++)
            (!1 & n || r >= n) &&
            Object.keys(__webpack_require__.O).every((e) => __webpack_require__.O[e](t[o]))
              ? t.splice(o--, 1)
              : ((a = !1), n < r && (r = n));
          if (a) {
            deferred.splice(s--, 1);
            var i = u();
            void 0 !== i && (e = i);
          }
        }
        return e;
      }
      n = n || 0;
      for (var s = deferred.length; s > 0 && deferred[s - 1][2] > n; s--)
        deferred[s] = deferred[s - 1];
      deferred[s] = [t, u, n];
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
    (() => {
      var e = { 589: 0 };
      __webpack_require__.O.j = (t) => 0 === e[t];
      var t = (t, u) => {
          var n,
            r,
            [a, o, i] = u,
            s = 0;
          if (a.some((t) => 0 !== e[t])) {
            for (n in o) __webpack_require__.o(o, n) && (__webpack_require__.m[n] = o[n]);
            if (i) var l = i(__webpack_require__);
          }
          for (t && t(u); s < a.length; s++)
            ((r = a[s]), __webpack_require__.o(e, r) && e[r] && e[r][0](), (e[r] = 0));
          return __webpack_require__.O(l);
        },
        u = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (u.forEach(t.bind(null, 0)), (u.push = t.bind(null, u.push.bind(u))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [994], () => __webpack_require__(978));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
