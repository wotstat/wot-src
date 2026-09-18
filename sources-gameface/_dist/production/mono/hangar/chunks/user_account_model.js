import { o as e, U as s, q as o } from "./vendor.js";
import {
  i as t,
  ci as n,
  ck as i,
  dn as r,
  dp as a,
  dq as c,
  dr as l,
  df as u,
  ds as p,
  dt as m,
  du as b,
  dv as d,
  dw as P,
  cj as f,
} from "./lib.js";
var v = ((e) => ((e.None = "None"), (e.Core = "Core"), (e.Pro = "Pro"), e))(v || {}),
  g = ((e) => ((e.Inactive = "Inactive"), (e.Active = "Active"), (e.Cancelled = "Cancelled"), e))(
    g || {},
  );
const C = b(
    P((e) => e > 0),
    d(f),
  ),
  k = [
    [r, a],
    [c, l],
    [u, p],
    [m, () => p(1)],
  ];
function A(e) {
  if (e) {
    const s = n(e, i());
    for (const [e, o] of k) {
      const t = Math.ceil(e(s));
      if (t > 0) return o(t);
    }
  }
}
var x = ((e) => (
  (e.Unlock = "unlock"),
  (e.UnlockSteamAndCn = "unlockSteamAndCn"),
  (e.UnlockPro = "unlockPro"),
  e
))(x || {});
const [y, I] = t("UserAccountProvider")(
  ({ observableModel: t, cleanup: n }) => {
    const i = t.object("userInfo"),
      r = t.object("subscriptions.wotPlus"),
      a = t.object("subscriptions.premiumAccount"),
      c = t.primitives(["isCnRealm", "isSteamPlatform"], "subscriptions"),
      l = t.arrayClone("subscriptions.wotPlus.benefits"),
      u = t.arrayClone("subscriptions.wotPlus.proBenefits"),
      p = { basic: e.box(A(C(a.get().expiryTime))), plus: e.box(A(C(r.get().expiryTime))) };
    const m = s(
        () => a.get().expiryTime,
        (e) => {
          p.basic.set(A(C(e)));
        },
      ),
      b = s(
        () => r.get().expiryTime,
        (e) => {
          p.plus.set(A(C(e)));
        },
      ),
      d = setInterval(function () {
        o(() => {
          (p.basic.set(A(C(a.get().expiryTime))), p.plus.set(A(C(r.get().expiryTime))));
        });
      }, 6e4);
    return (
      n(() => {
        (clearInterval(d), m(), b());
      }),
      {
        userInfo: i,
        premiums: p,
        wotPlus: r,
        premiumAccount: a,
        benefits: l,
        proBenefits: u,
        subscriptionPrimitives: c,
        getTooltipVariant: () => {
          const e = r.get().state,
            s = r.get().type;
          return e === g.Inactive && s === v.None && (c.isCnRealm.get() || c.isSteamPlatform.get())
            ? "unlockSteamAndCn"
            : e === g.Inactive && s === v.None
              ? "unlock"
              : e !== g.Inactive && s === v.Core
                ? "unlockPro"
                : "unlock";
        },
      }
    );
  },
  ({ externalModel: e }) => ({
    openAccountDashboard: e.createCallbackNoArgs("onOpenAccountDashboard"),
    openWotPlusSubscriptionPage: e.createCallbackNoArgs("subscriptions.onOpenWotPlus"),
    openPremiumSubscriptionPage: e.createCallbackNoArgs("subscriptions.onOpenPremium"),
  }),
);
export { x as T, y as U, g as W, v as a, I as u };
