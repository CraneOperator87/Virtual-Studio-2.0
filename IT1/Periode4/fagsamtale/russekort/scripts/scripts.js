// Event listeners
document.getElementById("navn").addEventListener("input", genererVisittkort);
document.getElementById("telefon").addEventListener("input", genererVisittkort);
document.getElementById("beskrivelse").addEventListener("input", genererVisittkort);
document.getElementById("trinn").addEventListener("input", genererVisittkort);
document.getElementById("farge").addEventListener("input", () => endreFarge(null));

document.getElementById("preset1").addEventListener("click", () => endreFarge("#ff0000"));
document.getElementById("preset2").addEventListener("click", () => endreFarge("#1500ff"));

document.getElementById("lagre-knapp").addEventListener("click", lagreVisittkort);
 
document.getElementsByClassName("visittkort") 


function genererVisittkort() {
    const navn = document.getElementById('navn').value.trim();
    const telefon = document.getElementById('telefon').value.trim();
    const beskrivelse = document.getElementById('beskrivelse').value.trim();
    const trinn = document.getElementById('trinn').value;
    const farge = document.getElementById('farge').value;
    const visittkortDiv = document.getElementById('visittkort');

    if (navn !== "" || telefon !== "" || beskrivelse !== "") { 
        visittkortDiv.innerHTML = `
            <h2>Visittkort</h2>
            <p><strong>Navn:</strong> ${navn}</p>
            <p><strong>Telefonnummer:</strong> ${telefon}</p>
            <p class="desc"><strong>Om personen:</strong> ${beskrivelse}</p>
            <p><strong>Trinn:</strong> ${trinn}</p>
        `;

        visittkortDiv.style.backgroundColor = farge;
        visittkortDiv.style.border = "1px solid black";
        visittkortDiv.style.display = "block"; 
    } else {
        visittkortDiv.style.display = "none";
        visittkortDiv.style.border = "none"; 
    }
}

function endreFarge(farge = null) {
    if (!farge) {
        farge = document.getElementById("farge").value;
    }
    const visittkortDiv = document.getElementById('visittkort');
    visittkortDiv.style.backgroundColor = farge;
    document.getElementById("farge").value = farge; // Oppdater fargeinputen
}

function lagreVisittkort() {
    const navn = document.getElementById('navn').value.trim();
    const telefon = document.getElementById('telefon').value.trim();
    const beskrivelse = document.getElementById('beskrivelse').value.trim();
    const trinn = document.getElementById('trinn').value;
    const farge = document.getElementById('farge').value;

    if (navn === "") return;

    const lagreCardsContainer = document.getElementById('lagrede-cards-container');

    const kloneKort = document.createElement("div");
    kloneKort.classList.add("visittkort");
    kloneKort.style.backgroundColor = farge;
    kloneKort.style.border = "1px solid black"; 
    kloneKort.innerHTML = `
        <h2>Visittkort</h2>
        <p><strong>Navn:</strong> ${navn}</p>
        <p><strong>Telefonnummer:</strong> ${telefon}</p>
        <p class="desc"><strong>Om personen:</strong> ${beskrivelse}</p>
        <p><strong>Trinn:</strong> ${trinn}</p>
    `;

    lagreCardsContainer.appendChild(kloneKort);
}
