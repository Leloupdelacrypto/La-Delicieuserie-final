(() => {
  "use strict";
  const production = location.origin === "https://www.ladelicieuserie.fr";
  const measurementId = "G-DM5CW16D3N";
  const disabled = "ga-disable-" + measurementId;
  let started = false;

  document.querySelectorAll("[data-cookies]").forEach(link => {
    link.addEventListener("click", event => {
      event.preventDefault();
      if (production && typeof window.__cmp === "function") {
        window.__cmp("showScreen");
        return;
      }
      const status = document.getElementById("cookie-status");
      status.textContent = production
        ? "Le gestionnaire de préférences est indisponible. Vous pouvez contacter l’atelier."
        : "La mesure d’audience est désactivée dans cet aperçu.";
      status.tabIndex = -1;
      status.focus();
    });
  });
  if (!production) return;

  window[disabled] = true;
  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function () { window.dataLayer.push(arguments); };
  window.gtag("consent", "default", {
    ad_storage: "denied", ad_user_data: "denied", ad_personalization: "denied",
    analytics_storage: "denied", functionality_storage: "denied",
    personalization_storage: "denied", security_storage: "granted"
  });

  function clearAnalyticsCookies() {
    const domains = ["", "; Domain=www.ladelicieuserie.fr", "; Domain=ladelicieuserie.fr"];
    for (const cookie of document.cookie.split(";")) {
      const name = cookie.trim().split("=")[0];
      if (name !== "_ga" && !name.startsWith("_ga_")) continue;
      for (const domain of domains) document.cookie = name + "=; Max-Age=0; Path=/; Secure; SameSite=Lax" + domain;
    }
  }
  function reconcile() {
    const cmp = window.__cmp;
    const allowed = cmp("consentStatus")?.consentExists === true &&
                    cmp("getCMPData")?.vendorConsents?.s26 === true;
    window[disabled] = !allowed;
    if (!allowed) {
      clearAnalyticsCookies();
      if (started) location.reload();
      return;
    }
    if (started) return;
    started = true;
    window.gtag("consent", "update", { analytics_storage: "granted" });
    window.gtag("js", new Date());
    window.gtag("config", measurementId, {
      allow_google_signals: false, allow_ad_personalization_signals: false,
      page_location: location.origin + location.pathname
    });
    const script = document.createElement("script");
    script.async = true;
    script.src = "https://www.googletagmanager.com/gtag/js?id=" + measurementId;
    document.head.append(script);
  }
  if (typeof window.__cmp === "function") {
    for (const event of ["settings", "consent", "consentcustom", "consentrejected", "consentapproved"]) {
      window.__cmp("addEventListener", [event, reconcile, false], null);
    }
    reconcile();
  }
})();
