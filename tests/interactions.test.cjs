const { test } = require("node:test");
const assert = require("node:assert/strict");
const { readFileSync } = require("node:fs");
const { join } = require("node:path");
const vm = require("node:vm");
const origin = "https://www.ladelicieuserie.fr";
const source = file => readFileSync(join(__dirname, "..", file), "utf8");

function consentPage(host = origin) {
  const handlers = {};
  const state = { choice: false, vendor: false, loads: [], deleted: [], reloads: 0 };
  const window = {
    __cmp(command, args) {
      if (command === "consentStatus") return { consentExists: state.choice };
      if (command === "getCMPData") return { vendorConsents: { s26: state.vendor } };
      if (command === "addEventListener") handlers[args[0]] = args[1];
    }
  };
  const document = {
    querySelectorAll: () => [], createElement: () => ({}),
    head: { append: script => state.loads.push(script.src) },
    get cookie() { return "_ga=sample; _ga_DM5CW16D3N=sample; necessary=ok"; },
    set cookie(string) { state.deleted.push(string); }
  };
  const location = { origin: host, pathname: "/devis/", reload: () => state.reloads++ };
  vm.runInNewContext(source("consent.js"), {window, document, location});
  return { state, window, change(choice, vendor) {
    Object.assign(state, {choice, vendor}); handlers.consent();
  }};
}
test("Analytics attend le choix et le fournisseur s26, puis cesse au retrait", () => {
  const page = consentPage();
  const {state,window} = page;
  page.change(false,true);
  page.change(true,false);
  assert.equal(state.loads.length,0);
  page.change(true,true);
  page.change(true,true);
  assert.deepEqual(state.loads,["https://www.googletagmanager.com/gtag/js?id=G-DM5CW16D3N"]);
  assert.equal(window["ga-disable-G-DM5CW16D3N"], false);
  page.change(true,false);
  assert.equal(window["ga-disable-G-DM5CW16D3N"], true);
  assert.equal(state.reloads,1);
  assert.ok(state.deleted.some(x=>x.startsWith("_ga_DM5CW16D3N=;")));
  assert.ok(!state.deleted.some(x=>x.startsWith("necessary=")));
});
test("Un aperçu ne charge pas Google", () => {
  assert.deepEqual(consentPage("https://preview.invalid").state.loads, []);
});

function quotePage(response, host = origin) {
  const handlers = {};
  const submit = {disabled:false};
  const status = {textContent:""};
  const state = {calls: [], redirect:null};
  const form = {
    action:"https://formsubmit.co/ladelicieuserie@gmail.com",
    elements:{occasion:{}, _honey:{value:""}, message:{value:"Message de test"}},
    querySelector: () => submit,
    addEventListener(event, handler) { handlers[event] = handler; }
  };
  const element = { addEventListener() {} };
  const document = {
    querySelector(selector) {
      return {".menu-toggle":element,"#navigation":element,"#form-status":status,"#quote-form":form}[selector];
    }, addEventListener() {}
  };
  const location = { origin:host, search:"?occasion=entreprise", assign(url) { state.redirect = url; }};
  async function fetch(url, options) {
    state.calls.push({url:String(url),options});
    return await response;
  }
  const window={matchMedia:()=>element,fetch,setTimeout};
  const FormData = class { constructor(element) { this.element = element; }};
  vm.runInNewContext(source("script.js"),{window,document,location,fetch,FormData,URL,URLSearchParams,AbortController,clearTimeout});
  return {state,form,submit,status,send:()=>handlers.submit({preventDefault(){}})};
}
test("Devis entreprise : POST privé, destinataire, prévention du double clic et confirmation", async () => {
  let resolve;
  const pending=new Promise(r=>{resolve=r;});
  const page=quotePage(pending);
  assert.equal(page.form.elements.occasion.value,"Entreprise");
  const first=page.send(); await page.send();
  assert.equal(page.state.calls.length,1);
  const {url,options}=page.state.calls[0];
  assert.equal(url,"https://formsubmit.co/ajax/ladelicieuserie@gmail.com");
  assert.equal(options.body.element,page.form);
  assert.equal(options.method,"POST");
  assert.equal(options.credentials,"omit");
  resolve({ok:true,json:async()=>({success:"true"})});
  await first;
  assert.equal(page.state.redirect,"/thanks.html");
});
test("Le prestataire en erreur ne produit pas de confirmation et permet de réessayer", async () => {
  for (const response of [{ok:false,json:async()=>({success:true})},{ok:true,json:async()=>({success:"false"})},
                          {ok:true,json:async()=>{throw new Error("réponse illisible");}}]) {
    const page=quotePage(response);
    await page.send();
    assert.equal(page.state.redirect,null);
    assert.equal(page.submit.disabled,false);
    assert.equal(page.form.elements.message.value,"Message de test");
    assert.match(page.status.textContent,/n’a pas pu être confirmée/);
  }
});
test("Le piège antispam et la prévisualisation n’émettent aucune soumission", async () => {
  const bot=quotePage({});
  bot.form.elements._honey.value="rempli";
  await bot.send();
  assert.equal(bot.state.calls.length,0);
  const preview=quotePage({}, "https://preview.invalid");
  await preview.send();
  assert.equal(preview.state.calls.length,0);
  assert.match(preview.status.textContent,/Aucun message/);
});
