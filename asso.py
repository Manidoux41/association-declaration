import os, json, zipfile, shutil, textwrap
base="/mnt/data/declaration-manifestation-app"
if os.path.exists(base): shutil.rmtree(base)
os.makedirs(base, exist_ok=True)

association = {
  "nom":"LA VOIX DES ENFANTS PLACÉS - VIENNE",
  "siren":"131725681",
  "rna":"W383010111",
  "siret":"13172568100012",
  "adresse":"3 rue de Gère",
  "codePostal":"38200",
  "ville":"Vienne",
  "telephone":"",
  "email":"",
  "representantLegal":"",
  "adresseRepresentant":"",
  "telephoneRepresentant":""
}
villes=[
{"ville":"Paris","departement":"Paris","codeDepartement":"75","prefecture":"Paris","adressePrefecture":"","emailPrefecture":"","telephonePrefecture":"","sourceOfficielle":""},
{"ville":"Marseille","departement":"Bouches-du-Rhône","codeDepartement":"13","prefecture":"Marseille","adressePrefecture":"","emailPrefecture":"","telephonePrefecture":"","sourceOfficielle":""},
{"ville":"Lyon","departement":"Rhône","codeDepartement":"69","prefecture":"Lyon","adressePrefecture":"","emailPrefecture":"","telephonePrefecture":"","sourceOfficielle":""},
{"ville":"Toulouse","departement":"Haute-Garonne","codeDepartement":"31","prefecture":"Toulouse","adressePrefecture":"","emailPrefecture":"","telephonePrefecture":"","sourceOfficielle":""},
{"ville":"Nice","departement":"Alpes-Maritimes","codeDepartement":"06","prefecture":"Nice","adressePrefecture":"","emailPrefecture":"","telephonePrefecture":"","sourceOfficielle":""},
{"ville":"Nantes","departement":"Loire-Atlantique","codeDepartement":"44","prefecture":"Nantes","adressePrefecture":"","emailPrefecture":"","telephonePrefecture":"","sourceOfficielle":""},
{"ville":"Montpellier","departement":"Hérault","codeDepartement":"34","prefecture":"Montpellier","adressePrefecture":"","emailPrefecture":"","telephonePrefecture":"","sourceOfficielle":""},
{"ville":"Strasbourg","departement":"Bas-Rhin","codeDepartement":"67","prefecture":"Strasbourg","adressePrefecture":"","emailPrefecture":"","telephonePrefecture":"","sourceOfficielle":""},
{"ville":"Bordeaux","departement":"Gironde","codeDepartement":"33","prefecture":"Bordeaux","adressePrefecture":"","emailPrefecture":"","telephonePrefecture":"","sourceOfficielle":""},
{"ville":"Lille","departement":"Nord","codeDepartement":"59","prefecture":"Lille","adressePrefecture":"","emailPrefecture":"","telephonePrefecture":"","sourceOfficielle":""},
{"ville":"Rennes","departement":"Ille-et-Vilaine","codeDepartement":"35","prefecture":"Rennes","adressePrefecture":"","emailPrefecture":"","telephonePrefecture":"","sourceOfficielle":""},
{"ville":"Toulon","departement":"Var","codeDepartement":"83","prefecture":"Toulon","adressePrefecture":"","emailPrefecture":"","telephonePrefecture":"","sourceOfficielle":""},
{"ville":"Reims","departement":"Marne","codeDepartement":"51","prefecture":"Châlons-en-Champagne","adressePrefecture":"","emailPrefecture":"","telephonePrefecture":"","sourceOfficielle":""},
{"ville":"Saint-Étienne","departement":"Loire","codeDepartement":"42","prefecture":"Saint-Étienne","adressePrefecture":"","emailPrefecture":"","telephonePrefecture":"","sourceOfficielle":""},
{"ville":"Le Havre","departement":"Seine-Maritime","codeDepartement":"76","prefecture":"Rouen","adressePrefecture":"","emailPrefecture":"","telephonePrefecture":"","sourceOfficielle":""},
{"ville":"Villeurbanne","departement":"Rhône","codeDepartement":"69","prefecture":"Lyon","adressePrefecture":"","emailPrefecture":"","telephonePrefecture":"","sourceOfficielle":""},
{"ville":"Dijon","departement":"Côte-d’Or","codeDepartement":"21","prefecture":"Dijon","adressePrefecture":"","emailPrefecture":"","telephonePrefecture":"","sourceOfficielle":""},
{"ville":"Angers","departement":"Maine-et-Loire","codeDepartement":"49","prefecture":"Angers","adressePrefecture":"","emailPrefecture":"","telephonePrefecture":"","sourceOfficielle":""},
{"ville":"Grenoble","departement":"Isère","codeDepartement":"38","prefecture":"Grenoble","adressePrefecture":"","emailPrefecture":"","telephonePrefecture":"","sourceOfficielle":""},
{"ville":"Nîmes","departement":"Gard","codeDepartement":"30","prefecture":"Nîmes","adressePrefecture":"","emailPrefecture":"","telephonePrefecture":"","sourceOfficielle":""},
{"ville":"Aix-en-Provence","departement":"Bouches-du-Rhône","codeDepartement":"13","prefecture":"Marseille","adressePrefecture":"","emailPrefecture":"","telephonePrefecture":"","sourceOfficielle":""},
{"ville":"Saint-Denis","departement":"La Réunion","codeDepartement":"974","prefecture":"Saint-Denis","adressePrefecture":"","emailPrefecture":"","telephonePrefecture":"","sourceOfficielle":""},
{"ville":"Clermont-Ferrand","departement":"Puy-de-Dôme","codeDepartement":"63","prefecture":"Clermont-Ferrand","adressePrefecture":"","emailPrefecture":"","telephonePrefecture":"","sourceOfficielle":""},
{"ville":"Le Mans","departement":"Sarthe","codeDepartement":"72","prefecture":"Le Mans","adressePrefecture":"","emailPrefecture":"","telephonePrefecture":"","sourceOfficielle":""},
{"ville":"Brest","departement":"Finistère","codeDepartement":"29","prefecture":"Quimper","adressePrefecture":"","emailPrefecture":"","telephonePrefecture":"","sourceOfficielle":""},
{"ville":"Tours","departement":"Indre-et-Loire","codeDepartement":"37","prefecture":"Tours","adressePrefecture":"","emailPrefecture":"","telephonePrefecture":"","sourceOfficielle":""},
{"ville":"Amiens","departement":"Somme","codeDepartement":"80","prefecture":"Amiens","adressePrefecture":"","emailPrefecture":"","telephonePrefecture":"","sourceOfficielle":""},
{"ville":"Annecy","departement":"Haute-Savoie","codeDepartement":"74","prefecture":"Annecy","adressePrefecture":"","emailPrefecture":"","telephonePrefecture":"","sourceOfficielle":""},
{"ville":"Limoges","departement":"Haute-Vienne","codeDepartement":"87","prefecture":"Limoges","adressePrefecture":"","emailPrefecture":"","telephonePrefecture":"","sourceOfficielle":""},
{"ville":"Perpignan","departement":"Pyrénées-Orientales","codeDepartement":"66","prefecture":"Perpignan","adressePrefecture":"","emailPrefecture":"","telephonePrefecture":"","sourceOfficielle":""}
]
for name,obj in [("association.json",association),("prefectures.json",villes)]:
    with open(os.path.join(base,name),"w",encoding="utf-8") as f: json.dump(obj,f,ensure_ascii=False,indent=2)

html = r'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Déclarations de manifestations — Association</title>
<style>
:root{--ink:#182522;--muted:#63716c;--line:#dce5df;--bg:#f3f7f4;--green:#176b53;--pale:#e7f2eb;--amber:#fff5dc}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 system-ui,-apple-system,Segoe UI,sans-serif}button,input,select,textarea{font:inherit}button{cursor:pointer;border:0;border-radius:9px;padding:10px 14px;background:var(--green);color:white;font-weight:700}button.secondary{background:white;color:var(--ink);border:1px solid var(--line)}button.danger{background:#fff0f0;color:#992e2e;border:1px solid #efcaca}.wrap{max-width:1200px;margin:auto;padding:26px 18px}.head{display:flex;align-items:center;gap:14px;margin-bottom:22px}.logo{background:var(--green);color:white;width:52px;height:52px;border-radius:15px;display:grid;place-items:center;font-weight:900;font-size:20px}.head h1{font-size:clamp(22px,3vw,31px);line-height:1.15;margin:0}.head p{margin:5px 0 0;color:var(--muted)}.head .new{margin-left:auto}.card{background:white;border:1px solid var(--line);border-radius:15px;padding:20px;margin-bottom:16px;box-shadow:0 4px 14px #18372b08}.association{display:grid;grid-template-columns:1fr auto;gap:8px 18px}.association h2{font-size:16px;margin:4px 0}.muted{color:var(--muted);font-size:13px}.ids{display:flex;gap:8px;align-items:center;flex-wrap:wrap}.ids span{background:#f1f6f2;padding:7px 10px;border-radius:8px;font-size:12px}.warning{background:var(--amber);border:1px solid #ebdcae;color:#6d5926;padding:13px 15px;border-radius:11px;font-size:13px;margin-bottom:18px}.tabs{display:flex;gap:5px;border-bottom:1px solid var(--line);margin-bottom:17px;overflow:auto}.tabs button{background:transparent;color:var(--muted);border-radius:8px 8px 0 0;border-bottom:2px solid transparent;white-space:nowrap}.tabs button.active{color:var(--green);border-color:var(--green);background:var(--pale)}.grid{display:grid;grid-template-columns:1fr 1fr;gap:16px;align-items:start}.fields{display:grid;grid-template-columns:1fr 1fr;gap:13px}.fields label,.org label{font-size:12px;font-weight:700;display:flex;flex-direction:column;gap:6px}.full{grid-column:1/-1}input,select,textarea{border:1px solid #d7e0da;border-radius:8px;padding:10px 11px;width:100%;background:#fff;color:var(--ink);min-width:0}input[readonly]{background:#f3f6f4;color:#65716c}textarea{resize:vertical}.section-title{display:flex;justify-content:space-between;align-items:center;margin-bottom:16px}.section-title h2{margin:0;font-size:20px}.eyebrow{font-size:10px;letter-spacing:1.3px;color:var(--green);font-weight:800;margin:0 0 4px}.org{padding:12px;border:1px solid var(--line);border-radius:10px;margin-bottom:10px;display:grid;gap:10px}.orgtop{display:flex;justify-content:space-between;align-items:center;font-size:13px}.actions{display:flex;gap:8px;flex-wrap:wrap;margin-top:16px}.actions button{flex:1}.message{background:var(--pale);color:var(--green);padding:11px 13px;border-radius:9px;margin-bottom:12px;font-size:13px}.errors{background:#fff0f0;color:#9b2525;padding:12px 15px;border-radius:9px;margin-bottom:12px}.document{max-width:850px;margin:auto;padding:35px 42px;border:1px solid var(--line);border-radius:8px;background:#fff;font:14px/1.7 Georgia,serif}.document h2{text-align:center;font:700 17px/1.4 Arial,sans-serif;margin:0 0 25px}.document p{margin:10px 0}.docwarn{background:var(--amber);padding:12px;font:12px/1.5 system-ui;border-radius:6px;margin-top:24px}.record{border:1px solid var(--line);border-radius:10px;padding:14px;display:flex;justify-content:space-between;align-items:center;gap:12px;margin:9px 0}.record h3{font-size:15px;margin:5px 0}.record p{font-size:12px;color:var(--muted);margin:0}.badge{font-size:10px;padding:4px 7px;border-radius:20px;background:#eff2f0}.record-actions{display:flex;gap:6px}.record-actions button{font-size:12px;padding:8px 10px}.hidden{display:none!important}footer{display:flex;justify-content:space-between;gap:12px;color:#7c8983;font-size:11px;padding:10px 2px} @media(max-width:800px){.grid{grid-template-columns:1fr}.head{flex-wrap:wrap}.head .new{margin-left:0}.association{grid-template-columns:1fr}.document{padding:22px 18px}}@media(max-width:520px){.fields{grid-template-columns:1fr}.full{grid-column:auto}.wrap{padding:16px 10px}.card{padding:15px}.record{align-items:flex-start}.record-actions{flex-direction:column}footer{flex-direction:column}}
@media print{body{background:white}.wrap{padding:0;max-width:none}.head,.association,.warning,.tabs,.no-print,footer{display:none!important}.card{border:0;box-shadow:none;padding:0}.document{border:0;padding:0;max-width:none}.docwarn{display:block}}
</style></head>
<body><main class="wrap">
<header class="head"><div class="logo">LV</div><div><h1>Déclarations de manifestations</h1><p>Préparer, vérifier et exporter les déclarations de l’association</p></div><button class="new no-print" id="newBtn">＋ Nouvelle déclaration</button></header>
<section class="card association"><div><p class="eyebrow">ASSOCIATION PRÉREMPLIE</p><h2 id="assocName"></h2><p class="muted" id="assocAddress"></p><p class="muted">Les coordonnées manquantes se modifient dans <code>association.json</code>.</p></div><div class="ids"><span>SIREN <b id="assocSiren"></b></span><span>RNA <b id="assocRna"></b></span></div></section>
<div class="warning"><b>À vérifier :</b> le référentiel contient 30 villes et ne remplace pas la vérification officielle de l’autorité compétente, des délais et des coordonnées. L’application ne transmet aucun formulaire automatiquement.</div>
<div id="message" class="message hidden"></div><div id="errors" class="errors hidden"></div>
<nav class="tabs no-print"><button data-tab="form" class="active">Formulaire</button><button data-tab="preview">Prévisualisation</button><button data-tab="history">Brouillons <span id="count">0</span></button><button data-tab="settings">Importer / exporter JSON</button></nav>
<section id="formTab" class="tab">
<div class="grid">
<div class="card"><div class="section-title"><div><p class="eyebrow">ÉVÉNEMENT</p><h2>Informations principales</h2></div></div>
<div class="fields">
<label class="full">Nom de la manifestation<input id="titre" placeholder="Ex. : Rassemblement pour les droits des enfants"></label>
<label class="full">Type d'événement<select id="type"><option>Rassemblement statique</option><option>Marche ou cortège</option><option>Autre manifestation</option></select></label>
<label class="full">Objet / motif<textarea id="objet" rows="3" placeholder="Décrivez l’objet et les revendications de la manifestation"></textarea></label>
<label>Ville du rassemblement<select id="ville"></select></label>
<label>Département<input id="departement" readonly></label>
<label>Préfecture du département<input id="prefecture" readonly></label>
<label>Destinataire<select id="autorite"><option value="Prefet">Madame ou Monsieur le Préfet</option><option value="Maire">Madame ou Monsieur le Maire</option></select></label>
<label class="full">Adresse postale de l’autorité (à vérifier)<input id="adresseAutorite" placeholder="À compléter depuis le site officiel"></label>
<label>Date de début<input id="dateDebut" type="date"></label><label>Date de fin (si différente)<input id="dateFin" type="date"></label>
<label>Heure de début<input id="heureDebut" type="time" value="14:00"></label><label>Heure de fin<input id="heureFin" type="time" value="17:00"></label>
<label>Nombre maximal estimé de personnes<input id="participants" type="number" min="1" value="50"></label>
<label>Ville de rédaction<input id="lieuRedaction" value="Vienne"></label><label>Date de rédaction<input id="dateRedaction" type="date"></label>
<label class="full">Lieux précis / places / rues / parcs / bâtiments publics<textarea id="lieux" rows="3" placeholder="Place, rue, boulevard, parc, abords de bâtiment public…"></textarea></label>
<label class="full">Itinéraire (pour une marche ou un cortège)<textarea id="itineraire" rows="2" placeholder="Départ, rues empruntées, arrivée"></textarea></label>
</div></div>
<div class="card"><div class="section-title"><div><p class="eyebrow">ORGANISATION</p><h2>Représentant et organisateurs</h2></div></div>
<div class="fields">
<label class="full">Représentant légal<input id="representant" placeholder="Prénom et nom"></label>
<label class="full">Adresse du représentant<input id="adresseRepresentant" placeholder="Adresse postale"></label>
<label>Téléphone du représentant<input id="telephoneRepresentant" placeholder="Téléphone"></label>
<label>E-mail de l’association<input id="emailAssociation" type="email" placeholder="Facultatif"></label>
</div><hr style="border:0;border-top:1px solid var(--line);margin:18px 0">
<div class="section-title"><h2 style="font-size:16px">Organisateurs mandatés</h2><button type="button" class="secondary no-print" id="addOrg">＋ Ajouter</button></div>
<div id="orgs"></div>
<label style="font-size:12px;font-weight:700;display:flex;flex-direction:column;gap:6px">Notes internes<textarea id="notes" rows="2" placeholder="Notes de préparation, non incluses dans la lettre"></textarea></label>
<div class="actions no-print"><button id="saveBtn">💾 Enregistrer le brouillon</button><button class="secondary" id="readyBtn">Marquer prête à relire</button></div>
</div></div></section>
<section id="previewTab" class="tab hidden"><div class="card"><div class="section-title no-print"><div><p class="eyebrow">DOCUMENT GÉNÉRÉ</p><h2>Prévisualisation</h2></div><div class="actions" style="margin:0"><button id="printBtn">Imprimer / PDF</button><button class="secondary" id="textBtn">Exporter TXT</button><button class="secondary" id="jsonOneBtn">Exporter JSON</button></div></div><article class="document" id="document"></article><div class="actions no-print"><button id="saveFromPreview">Enregistrer le brouillon</button></div></div></section>
<section id="historyTab" class="tab hidden"><div class="card"><div class="section-title"><div><p class="eyebrow">STOCKAGE SUR CET APPAREIL</p><h2>Brouillons et historique</h2></div><input id="search" placeholder="Rechercher…" style="max-width:260px"></div><div id="records"></div><p class="muted">Les données restent dans ce navigateur. Exportez régulièrement une sauvegarde JSON ; elles ne sont pas synchronisées entre appareils.</p></div></section>
<section id="settingsTab" class="tab hidden"><div class="grid"><div class="card"><h2>Importer un référentiel JSON</h2><p class="muted">Charge un fichier JSON de préfectures/villes. Champs attendus : ville, departement, codeDepartement, prefecture et, facultativement, adressePrefecture, emailPrefecture, telephonePrefecture, sourceOfficielle.</p><input id="refFile" type="file" accept=".json,application/json"><div class="actions"><button id="importRef">Importer le référentiel</button><button class="secondary" id="exportRef">Télécharger le référentiel actuel</button></div><p id="refStatus" class="muted"></p></div><div class="card"><h2>Importer / exporter les brouillons</h2><p class="muted">Le fichier de sauvegarde contient les déclarations enregistrées dans ce navigateur.</p><input id="backupFile" type="file" accept=".json,application/json"><div class="actions"><button id="importBackup">Importer une sauvegarde</button><button class="secondary" id="exportBackup">Exporter tous les brouillons</button></div><p id="backupStatus" class="muted"></p><hr style="border:0;border-top:1px solid var(--line);margin:20px 0"><h3>Fichiers JSON</h3><div class="actions"><a href="association.json" download><button type="button" class="secondary">association.json</button></a><a href="prefectures.json" download><button type="button" class="secondary">prefectures.json</button></a></div></div></div></section>
<footer><span>Outil local de préparation documentaire</span><span>Aucun envoi automatique · Vérification humaine avant dépôt</span></footer>
</main>
<script>
const KEY="declarations-manifestations-v1", REFKEY="declarations-prefectures-v1";
let association={}, cities=[], records=[], activeId=null, organizers=[{nom:"",adresse:"",telephone:"",email:""}], status="Brouillon";
const $=id=>document.getElementById(id);
const esc=s=>String(s??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const today=()=>new Date().toISOString().slice(0,10);
function loadLocal(){try{records=JSON.parse(localStorage.getItem(KEY)||"[]")}catch{records=[]}}
function persist(){localStorage.setItem(KEY,JSON.stringify(records));$("count").textContent=records.length;renderRecords()}
function download(name,content,type="application/json;charset=utf-8"){const b=new Blob([content],{type}),u=URL.createObjectURL(b),a=document.createElement("a");a.href=u;a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(u),1000)}
async function init(){try{association=await fetch("./association.json").then(r=>{if(!r.ok)throw Error();return r.json()})}catch{association={nom:"LA VOIX DES ENFANTS PLACÉS - VIENNE",siren:"131725681",rna:"W383010111",adresse:"3 rue de Gère",codePostal:"38200",ville:"Vienne"}}
try{cities=JSON.parse(localStorage.getItem(REFKEY)||"null")||await fetch("./prefectures.json").then(r=>r.json())}catch{cities=[]}
$("assocName").textContent=association.nom;$("assocAddress").textContent=`${association.adresse}, ${association.codePostal} ${association.ville}`;$("assocSiren").textContent=association.siren;$("assocRna").textContent=association.rna;
$("dateRedaction").value=today();renderCities();loadLocal();persist();renderOrgs();updateCity();renderPreview();wire()}
function renderCities(){const select=$("ville");select.innerHTML="";const defaultOpt=document.createElement("option");defaultOpt.value="";defaultOpt.textContent="Choisir une ville";select.append(defaultOpt);cities.forEach(c=>{const o=document.createElement("option");o.value=c.ville;o.textContent=`${c.ville} — ${c.departement} (${c.codeDepartement})`;select.append(o)});if(cities.some(c=>c.ville==="Vienne"))select.value="Vienne"}
function updateCity(){const c=cities.find(x=>x.ville===$("ville").value);$("departement").value=c?`${c.departement} (${c.codeDepartement})`:"";$("prefecture").value=c?c.prefecture:"";if(c&&$("adresseAutorite").value==="")$("adresseAutorite").value=c.adressePrefecture||""}
function renderOrgs(){ $("orgs").innerHTML=organizers.map((o,i)=>`<div class="org"><div class="orgtop"><b>Organisateur ${i+1}</b>${organizers.length>1?`<button class="danger no-print" data-remove="${i}" type="button">Retirer</button>`:""}</div><label>Prénom et nom<input data-org="${i}" data-key="nom" value="${esc(o.nom)}" placeholder="Nom complet"></label><label>Domicile<input data-org="${i}" data-key="adresse" value="${esc(o.adresse)}" placeholder="Adresse postale"></label><label>Téléphone<input data-org="${i}" data-key="telephone" value="${esc(o.telephone)}" placeholder="Moyen de contact"></label><label>E-mail (facultatif)<input data-org="${i}" data-key="email" value="${esc(o.email)}" placeholder="adresse@exemple.fr"></label></div>`).join("");$("orgs").querySelectorAll("[data-org]").forEach(el=>el.addEventListener("input",()=>{organizers[+el.dataset.org][el.dataset.key]=el.value;renderPreview()}));$("orgs").querySelectorAll("[data-remove]").forEach(el=>el.addEventListener("click",()=>{organizers.splice(+el.dataset.remove,1);renderOrgs();renderPreview()}))}
function val(id){return $(id).value.trim()}
function getData(){const c=cities.find(x=>x.ville===val("ville"));return {titre:val("titre"),type:val("type"),objet:val("objet"),ville:val("ville"),departement:c?.departement||"",codeDepartement:c?.codeDepartement||"",prefecture:c?.prefecture||"",autorite:val("autorite"),adresseAutorite:val("adresseAutorite"),dateDebut:val("dateDebut"),dateFin:val("dateFin"),heureDebut:val("heureDebut"),heureFin:val("heureFin"),participants:Number(val("participants")),lieuRedaction:val("lieuRedaction"),dateRedaction:val("dateRedaction"),lieux:val("lieux"),itineraire:val("itineraire"),representant:val("representant"),adresseRepresentant:val("adresseRepresentant"),telephoneRepresentant:val("telephoneRepresentant"),emailAssociation:val("emailAssociation"),organisateurs:organizers.map(x=>({...x})),notes:val("notes")}}
function validate(d){const e=[];if(!d.titre)e.push("Indique le nom de la manifestation.");if(!d.objet)e.push("Décris l’objet de la manifestation.");if(!d.dateDebut)e.push("Choisis la date de début.");if(!d.heureDebut||!d.heureFin)e.push("Indique les heures de début et de fin.");if(!d.ville)e.push("Choisis une ville.");if(!d.lieux)e.push("Précise les lieux d’occupation du domaine public.");if(!(d.participants>=1))e.push("Le nombre maximal doit être au moins égal à 1.");if(!d.representant)e.push("Complète le représentant légal de l’association.");if(!d.organisateur||!d.organisateurs.length||!d.organisateurs[0].nom||!d.organisateurs[0].adresse||!d.organisateurs[0].telephone)e.push("Complète les nom, domicile et contact d’au moins un organisateur.");if(d.dateFin&&d.dateFin<d.dateDebut)e.push("La date de fin ne peut pas précéder la date de début.");if(d.heureFin&&d.heureDebut&&d.heureFin<d.heureDebut&&!d.dateFin)e.push("L’heure de fin précède l’heure de début : vérifie les dates.");return e}
function displayDate(s){if(!s)return "[à compléter]";const [y,m,d]=s.split("-");return `${d}/${m}/${y}`}
function documentText(d){const assoc=association;const orgs=d.organisateurs.map(o=>`${o.nom} — ${o.adresse} — ${o.telephone}${o.email?" — "+o.email:""}`).join("\n");const dates=d.dateFin&&d.dateFin!==d.dateDebut?`du ${displayDate(d.dateDebut)} au ${displayDate(d.dateFin)} inclus`:`le ${displayDate(d.dateDebut)}`;const recipient=d.autorite==="Maire"?"Madame ou Monsieur le Maire":"Madame ou Monsieur le Préfet";return `${assoc.nom}\n${assoc.adresse}, ${assoc.codePostal} ${assoc.ville}\nTéléphone : ${assoc.telephone||"[à compléter]"}${assoc.email?"\nE-mail : "+assoc.email:""}\nSIREN : ${assoc.siren} — RNA : ${assoc.rna}\n\nReprésentant légal : ${d.representant}\nAdresse : ${d.adresseRepresentant||"[à compléter]"}\nTéléphone : ${d.telephoneRepresentant||"[à compléter]"}\n\nÀ ${d.lieuRedaction||"[lieu]"}, le ${displayDate(d.dateRedaction)}\n\nÀ l’attention de ${recipient}\n${d.adresseAutorite||"[adresse officielle de l’autorité à vérifier]"}\n\nObjet : Déclaration préalable d’une manifestation sur la voie publique\n\nMadame, Monsieur,\n\nJe vous informe que l’association ${assoc.nom} souhaite organiser ${d.type.toLowerCase()}, sous l’appellation « ${d.titre} ».\n\nObjet de l’événement : ${d.objet}\nPériode : ${dates}\nLieu(x) : ${d.ville} (${d.departement}) — ${d.lieux}\n\nLe bon déroulement de la manifestation requiert une occupation temporaire du domaine public :\nDate(s) : ${dates}\nHeure de début : ${d.heureDebut}\nHeure de fin : ${d.heureFin}\nEndroit(s) : ${d.lieux}\n${d.itineraire?"Itinéraire : "+d.itineraire+"\n":""}\nJ’estime le nombre maximum de personnes susceptibles d’être rassemblées au même endroit au même moment à ${d.participants}.\n\nPersonnes mandatées pour assurer la bonne organisation :\n${orgs||"[organisateurs à compléter]"}\n\nJe me tiens à votre disposition pour tout renseignement complémentaire que vous jugerez utile.\n\nJe vous prie d’agréer, Madame, Monsieur, l’assurance de ma considération distinguée.\n\n${d.organisateurs[0]?.nom||d.representant}\nSignature :\n\nDocument préparatoire à vérifier avant signature et dépôt. La génération ne vaut ni dépôt ni autorisation.`}
function renderPreview(){const d=getData();const txt=documentText(d);$("document").innerHTML=txt.split("\n").map((line,i)=>{if(i===0)return `<h2>${esc(line)}</h2>`;if(!line)return "<p></p>";if(line.startsWith("Objet :")||line.startsWith("Objet de l’événement:")||line.startsWith("Période :")||line.startsWith("Lieu(x) :")||line.startsWith("Heure de")||line.startsWith("Date(s) :")||line.startsWith("Endroit(s) :")||line.startsWith("Itinéraire :")||line.startsWith("J’estime")||line.startsWith("Personnes mandatées"))return `<p><b>${esc(line.split(":")[0]+(line.includes(":")?":":""))}</b>${esc(line.includes(":")?line.slice(line.indexOf(":")+1):"")}</p>`;if(line.startsWith("Document préparatoire"))return `<div class="docwarn">${esc(line)}</div>`;return `<p>${esc(line)}</p>`}).join("")}
function showMessage(s){$("message").textContent=s;$("message").classList.remove("hidden");$("errors").classList.add("hidden")}
function showErrors(es){$("errors").innerHTML="<b>À corriger :</b><ul>"+es.map(x=>`<li>${esc(x)}</li>`).join("")+"</ul>";$("errors").classList.remove("hidden");$("message").classList.add("hidden")}
function save(newStatus="Brouillon"){const d=getData(),e=validate(d);if(e.length){showErrors(e);return}const now=new Date().toISOString(),old=records.find(x=>x.id===activeId);const item={...d,id:activeId||crypto.randomUUID(),statut:newStatus,createdAt:old?.createdAt||now,updatedAt:now};records=[item,...records.filter(x=>x.id!==item.id)];activeId=item.id;status=newStatus;persist();showMessage(newStatus==="Brouillon"?"Brouillon enregistré dans ce navigateur.":"Déclaration marquée prête à relire.");}
function fillForm(d){const ids=["titre","type","objet","ville","autorite","adresseAutorite","dateDebut","dateFin","heureDebut","heureFin","participants","lieuRedaction","dateRedaction","lieux","itineraire","representant","adresseRepresentant","telephoneRepresentant","emailAssociation","notes"];ids.forEach(id=>{if(d[id]!==undefined)$(id).value=d[id]});activeId=d.id||null;status=d.statut||"Brouillon";organizers=d.organisateurs?.length?d.organisateurs:[{nom:"",adresse:"",telephone:"",email:""}];renderOrgs();updateCity();renderPreview();switchTab("form")}
function renderRecords(){const q=($("search")?.value||"").toLowerCase();const arr=records.filter(x=>`${x.titre} ${x.ville} ${x.departement}`.toLowerCase().includes(q));$("records").innerHTML=arr.length?arr.map(x=>`<div class="record"><div><span class="badge">${esc(x.statut)}</span><h3>${esc(x.titre)}</h3><p>${esc(x.ville)} · ${esc(displayDate(x.dateDebut))} · ${esc(x.heureDebut)}–${esc(x.heureFin)}</p></div><div class="record-actions"><button class="secondary" data-open="${x.id}">Ouvrir</button><button class="danger" data-delete="${x.id}">Supprimer</button></div></div>`).join(""):'<p class="muted">Aucun brouillon enregistré.</p>';$("records").querySelectorAll("[data-open]").forEach(b=>b.onclick=()=>{const x=records.find(r=>r.id===b.dataset.open);if(x)fillForm(x)});$("records").querySelectorAll("[data-delete]").forEach(b=>b.onclick=()=>{if(confirm("Supprimer ce brouillon de cet appareil ?")){records=records.filter(r=>r.id!==b.dataset.delete);if(activeId===b.dataset.delete){activeId=null}persist();showMessage("Brouillon supprimé.")}})}
function switchTab(name){document.querySelectorAll(".tabs button").forEach(b=>b.classList.toggle("active",b.dataset.tab===name));document.querySelectorAll(".tab").forEach(s=>s.classList.add("hidden"));$(name+"Tab").classList.remove("hidden");if(name==="preview")renderPreview();if(name==="history")renderRecords()}
function wire(){document.querySelectorAll("[data-tab]").forEach(b=>b.onclick=()=>switchTab(b.dataset.tab));$("ville").onchange=()=>{updateCity();renderPreview()};$("addOrg").onclick=()=>{organizers.push({nom:"",adresse:"",telephone:"",email:""});renderOrgs()};$("saveBtn").onclick=()=>save("Brouillon");$("readyBtn").onclick=()=>save("Prête à relire");$("saveFromPreview").onclick=()=>save("Brouillon");$("printBtn").onclick=()=>window.print();$("textBtn").onclick=()=>download(`declaration-${slug(val("titre"))}.txt`,documentText(getData()),"text/plain;charset=utf-8");$("jsonOneBtn").onclick=()=>download(`declaration-${slug(val("titre"))}.json`,JSON.stringify({...getData(),id:activeId,statut:status},null,2));$("newBtn").onclick=()=>{activeId=null;status="Brouillon";document.querySelectorAll("#formTab input,#formTab textarea").forEach(el=>{if(el.id!=="heureDebut"&&el.id!=="heureFin"&&el.id!=="participants"&&el.id!=="lieuRedaction"&&el.id!=="dateRedaction")el.value=""});$("type").value="Rassemblement statique";$("autorite").value="Prefet";$("heureDebut").value="14:00";$("heureFin").value="17:00";$("participants").value=50;$("lieuRedaction").value="Vienne";$("dateRedaction").value=today();organizers=[{nom:association.representantLegal||"",adresse:association.adresseRepresentant||"",telephone:association.telephoneRepresentant||"",email:""}];renderOrgs();updateCity();switchTab("form")};["titre","type","objet","autorite","adresseAutorite","dateDebut","dateFin","heureDebut","heureFin","participants","lieuRedaction","dateRedaction","lieux","itineraire","representant","adresseRepresentant","telephoneRepresentant","emailAssociation","notes"].forEach(id=>$(id).addEventListener("input",renderPreview));$("search").oninput=renderRecords;
$("importRef").onclick=async()=>{try{const f=$("refFile").files[0];if(!f)throw Error("Choisis un fichier JSON.");const x=JSON.parse(await f.text());if(!Array.isArray(x)||!x.every(c=>c.ville&&c.departement&&c.codeDepartement&&c.prefecture))throw Error("Format invalide : les champs ville, departement, codeDepartement et prefecture sont requis.");cities=x;localStorage.setItem(REFKEY,JSON.stringify(cities));renderCities();$("refStatus").textContent=`${cities.length} entrées importées.`;updateCity()}catch(e){$("refStatus").textContent=e.message}};
$("exportRef").onclick=()=>download("prefectures.json",JSON.stringify(cities,null,2));
$("exportBackup").onclick=()=>download("sauvegarde-declarations.json",JSON.stringify(records,null,2));
$("importBackup").onclick=async()=>{try{const f=$("backupFile").files[0];if(!f)throw Error("Choisis un fichier JSON.");const x=JSON.parse(await f.text());if(!Array.isArray(x))throw Error("Le fichier doit contenir un tableau de déclarations.");if(!confirm("Importer "+x.length+" déclaration(s) ? Les identifiants existants seront remplacés en cas de doublon."))return;records=[...x.filter(r=>r.id),...records.filter(r=>!x.some(y=>y.id===r.id))];persist();$("backupStatus").textContent=`${x.length} déclaration(s) importée(s).`}catch(e){$("backupStatus").textContent=e.message}}}
function slug(s){return String(s||"manifestation").normalize("NFD").replace(/[\u0300-\u036f]/g,"").toLowerCase().replace(/[^a-z0-9]+/g,"-").replace(/^-|-$/g,"")||"manifestation"}
init();
</script></body></html>'''
with open(os.path.join(base,"index.html"),"w",encoding="utf-8") as f: f.write(html)

readme = """# Application de préparation des déclarations de manifestations

Application web statique, sans Next.js, sans installation et sans serveur. Elle fonctionne dans un navigateur moderne.

## Démarrage rapide
1. Décompressez l’archive.
2. Ouvrez `index.html` dans votre navigateur.

Si le navigateur bloque le chargement des fichiers JSON via `file://`, lancez un serveur local dans ce dossier :
- Python : `python3 -m http.server 8000`
- Puis ouvrez `http://localhost:8000`

## Fichiers JSON
- `association.json` : coordonnées de l’association préremplies.
- `prefectures.json` : référentiel de 30 grandes villes et préfectures correspondantes. Les champs d’adresse, e-mail, téléphone et source officielle sont laissés vides volontairement pour ne pas inventer de coordonnées.

Complétez `association.json` avec les coordonnées réelles du représentant légal, le téléphone et l’e-mail de l’association.

## Fonctionnalités
- Formulaire guidé avec champs obligatoires vérifiés.
- Génération d’une lettre à partir des informations saisies.
- Prévisualisation.
- Impression ou « Enregistrer au format PDF » depuis la fenêtre d’impression du navigateur.
- Export TXT et JSON d’une déclaration.
- Brouillons/historique conservés dans `localStorage`.
- Import/export JSON du référentiel et des brouillons.
- Aucune transmission automatique à une mairie ou préfecture.

## Données et confidentialité
Les déclarations sont conservées dans le stockage local du navigateur sur l’appareil courant. Elles ne sont pas envoyées vers un serveur et ne se synchronisent pas entre appareils. Exportez une sauvegarde JSON régulièrement.

## Limites
Le référentiel couvre 30 villes seulement, et la commune de rassemblement n’est pas toujours la ville où se trouve la préfecture. Vérifiez l’autorité compétente, les délais de déclaration et les consignes locales auprès des sources officielles. Le document généré est préparatoire et ne vaut pas dépôt ni autorisation.
"""
with open(os.path.join(base,"README.md"),"w",encoding="utf-8") as f: f.write(readme)

zip_path="/mnt/data/declaration-manifestation-app.zip"
if os.path.exists(zip_path): os.remove(zip_path)
with zipfile.ZipFile(zip_path,"w",zipfile.ZIP_DEFLATED) as z:
    for root,dirs,names in os.walk(base):
        for name in names:
            full=os.path.join(root,name)
            z.write(full,os.path.relpath(full,os.path.dirname(base)))
print("Created", zip_path, os.path.getsize(zip_path), "bytes")
