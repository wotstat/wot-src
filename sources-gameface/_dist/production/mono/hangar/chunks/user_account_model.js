import { o as e, U as s, q as o } from "./vendor.js";
import {
  i as t,
  ci as n,
  ck as i,
  dw as a,
  dk as r,
  dx as c,
  dy as l,
  df as u,
  dz as p,
  dA as m,
  dB as b,
  dC as d,
  dD as P,
  cj as f,
} from "./lib.js";
var g = ((e) => ((e.None = "None"), (e.Core = "Core"), (e.Pro = "Pro"), e))(g || {}),
  v = ((e) => ((e.Inactive = "Inactive"), (e.Active = "Active"), (e.Cancelled = "Cancelled"), e))(
    v || {},
  );
const C = b(
    P((e) => e > 0),
    d(f),
  ),
  k = [
    [a, r],
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
      a = t.object("subscriptions.wotPlus"),
      r = t.object("subscriptions.premiumAccount"),
      c = t.primitives(["isCnRealm", "isSteamPlatform"], "subscriptions"),
      l = t.arrayClone("subscriptions.wotPlus.benefits"),
      u = t.arrayClone("subscriptions.wotPlus.proBenefits"),
      p = { basic: e.box(A(C(r.get().expiryTime))), plus: e.box(A(C(a.get().expiryTime))) };
    const m = s(
        () => r.get().expiryTime,
        (e) => {
          p.basic.set(A(C(e)));
        },
      ),
      b = s(
        () => a.get().expiryTime,
        (e) => {
          p.plus.set(A(C(e)));
        },
      ),
      d = setInterval(function () {
        o(() => {
          (p.basic.set(A(C(r.get().expiryTime))), p.plus.set(A(C(a.get().expiryTime))));
        });
      }, 6e4);
    return (
      n(() => {
        (clearInterval(d), m(), b());
      }),
      {
        userInfo: i,
        premiums: p,
        wotPlus: a,
        premiumAccount: r,
        benefits: l,
        proBenefits: u,
        subscriptionPrimitives: c,
        getTooltipVariant: () => {
          const e = a.get().state,
            s = a.get().type;
          return e === v.Inactive && s === g.None && (c.isCnRealm.get() || c.isSteamPlatform.get())
            ? "unlockSteamAndCn"
            : e === v.Inactive && s === g.None
              ? "unlock"
              : e !== v.Inactive && s === g.Core
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
export { x as T, y as U, v as W, g as a, I as u };
