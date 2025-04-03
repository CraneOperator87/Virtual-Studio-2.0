let bøker;

function hentBøker() {
  fetch("boker.json")
    .then((response) => response.json())
    .then((data) => {
      bøker = data;
      visBøker();
      oppdaterHandlekurv();
    })
    .catch((error) => {
      console.error("Feil ved henting av bøker:", error);
    });
}


let fjernAlleBoker = document.querySelector("#delete");
fjernAlleBoker.addEventListener("click", fjernBoker);

// Initialize handlekurv from localStorage or as an empty array
let handlekurv = JSON.parse(localStorage.getItem("handlekurv")) || [];

function visBøker() {
  const bokListe = document.querySelector("#bok-liste");
  bokListe.innerHTML = "";
  for (const bok of bøker) {
    const bokElement = document.createElement("div");
    bokElement.classList.add("bok");
    bokElement.innerHTML = `
      <h3>${bok.tittel}</h3>
      <p>Av: ${bok.forfatter}</p>
      <p>Pris: ${bok.pris} NOK</p>
    `;
    const knapp = document.createElement("button");
    knapp.textContent = "Legg til i handlekurv";
    knapp.addEventListener("click", function () {
      leggTilIHandlekurv(bok.id);
    });
    bokElement.appendChild(knapp);
    bokListe.appendChild(bokElement);
  }
}

function leggTilIHandlekurv(bokId) {
  let valgtBok = null;
  for (const bok of bøker) {
    if (bok.id === bokId) {
      valgtBok = bok;
      break;
    }
  }
  if (valgtBok) {
    handlekurv.push(valgtBok);
    oppdaterHandlekurv();
  }
}

function oppdaterHandlekurv() {
  localStorage.setItem("handlekurv", JSON.stringify(handlekurv));
  oppdaterHTMLHandlekurv();
}

function oppdaterHTMLHandlekurv() {
  const handlekurvListe = document.querySelector("#handlekurv-liste");
  const totalPrisElement = document.querySelector("#totalpris");

  handlekurvListe.innerHTML = "";
  let total = 0;

  for (const bok of handlekurv) {
    const listeElement = document.createElement("li");
    listeElement.textContent = `${bok.tittel} - ${bok.pris} NOK`;
    handlekurvListe.appendChild(listeElement);
    total += bok.pris;
  }

  totalPrisElement.textContent = total;
}

function fjernBoker () {
  handlekurv = []
  oppdaterHandlekurv()
}

hentBøker();
visBøker();
oppdaterHandlekurv();