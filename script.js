(() => {
  "use strict";

  const toggle = document.querySelector(".menu-toggle");
  const menu = document.querySelector("#navigation");
  toggle.hidden = false;
  function closeMenu() {
    toggle.setAttribute("aria-expanded", "false");
  }
  toggle.addEventListener("click", () => {
    toggle.setAttribute("aria-expanded", String(toggle.getAttribute("aria-expanded") !== "true"));
  });
  menu.addEventListener("click", closeMenu);
  document.addEventListener("click", event => {
    if (!event.target.closest(".masthead")) closeMenu();
  });
  document.addEventListener("keydown", event => {
    if (event.key === "Escape" && toggle.getAttribute("aria-expanded") === "true") {
      closeMenu();
      toggle.focus();
    }
  });
  window.matchMedia("(max-width: 1040px)").addEventListener("change", closeMenu);

  const dialog = document.querySelector(".lightbox");
  if (dialog && typeof dialog.showModal === "function") {
    const links = [...document.querySelectorAll(".zoom-link")];
    const photo = dialog.querySelector("img");
    const caption = dialog.querySelector("figcaption");
    let index = 0;
    let opener;
    function showPhoto(next) {
      index = (next + links.length) % links.length;
      const link = links[index];
      photo.alt = link.querySelector("img").alt;
      photo.src = link.href;
      caption.textContent = link.dataset.caption + " · " + (index + 1) + " / " + links.length;
    }
    for (const [i, link] of links.entries()) {
      link.addEventListener("click", event => {
        if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
        event.preventDefault();
        opener = link;
        showPhoto(i);
        dialog.showModal();
      });
    }
    dialog.querySelector(".lightbox-close").addEventListener("click", () => dialog.close());
    dialog.addEventListener("click", event => {
      const button = event.target.closest("[data-step]");
      if (button) showPhoto(index + Number(button.dataset.step));
      if (event.target !== dialog) return;
      const rect = dialog.getBoundingClientRect();
      if (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom) dialog.close();
    });
    dialog.addEventListener("keydown", event => {
      if (event.key === "ArrowRight" || event.key === "ArrowLeft") {
        event.preventDefault();
        showPhoto(index + (event.key === "ArrowRight" ? 1 : -1));
      }
    });
    dialog.addEventListener("close", () => {
      photo.removeAttribute("src");
      if (opener) opener.focus();
    });
  }

  const form = document.querySelector("#quote-form");
  if (!form) return;
  const status = document.querySelector("#form-status");
  const submit = form.querySelector('[type="submit"]');
  const production = location.origin === "https://www.ladelicieuserie.fr";
  const occasions = { entreprise: "Entreprise", famille: "Fête de famille", mariage: "Mariage" };
  const occasion = new URLSearchParams(location.search).get("occasion");
  if (Object.hasOwn(occasions, occasion)) form.elements.occasion.value = occasions[occasion];
  if (!production) {
    submit.textContent = "Tester la demande";
    status.textContent = "Aperçu : ce formulaire de démonstration ne transmet aucune donnée.";
  }

  form.addEventListener("submit", async event => {
    if (production && !window.fetch) return; // Le POST HTML reste utilisable sans amélioration JS.
    event.preventDefault();
    if (submit.disabled) return;
    if (!production) {
      status.textContent = "Les champs sont valides. Aucun message n’a été envoyé depuis cet aperçu.";
      return;
    }
    if (form.elements._honey.value) {
      status.textContent = "Impossible de traiter cette demande. Vous pouvez contacter directement l’atelier.";
      return;
    }
    submit.disabled = true;
    status.textContent = "Transmission de votre demande…";
    const controller = new AbortController();
    const timeout = window.setTimeout(() => controller.abort(), 20000);
    try {
      const endpoint = new URL(form.action);
      endpoint.pathname = "/ajax" + endpoint.pathname;
      const response = await fetch(endpoint, {
        method: "POST", body: new FormData(form), headers: { Accept: "application/json" },
        credentials: "omit", referrerPolicy: "origin", signal: controller.signal
      });
      const result = await response.json();
      if (!response.ok || ![true, "true"].includes(result.success)) throw new Error("Envoi non confirmé");
      location.assign("/thanks.html");
    } catch {
      submit.disabled = false;
      status.textContent = "La transmission n’a pas pu être confirmée. Vos champs sont conservés. Joignez l’atelier au 06 17 41 97 61 ou à ladelicieuserie@gmail.com.";
    } finally {
      clearTimeout(timeout);
    }
  });
})();
