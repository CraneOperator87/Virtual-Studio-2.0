document.getElementById("navn").addEventListener("input", genererVisittkort);
document.getElementById("telefon").addEventListener("input", genererVisittkort);
document.getElementById("beskrivelse").addEventListener("input", genererVisittkort);
document.getElementById("trinn").addEventListener("input", genererVisittkort);

document.getElementById("farge").addEventListener("input", endreFarge);


function genererVisittkort() {
    const navn = document.getElementById('navn').value;
    const telefon = document.getElementById('telefon').value;
    const beskrivelse = document.getElementById('beskrivelse').value;
    const trinn = document.getElementById('trinn').value;

    const farge = document.getElementById('farge').value;

    const visittkortDiv = document.getElementById('visittkort');

    visittkortDiv.innerHTML = `
        <h2>Visittkort</h2>
        <p><strong>Navn:</strong> ${navn}</p>
        <p><strong>Telefonnummer:</strong> ${telefon}</p>
        <p class="desc"><strong>Om personen:</strong> ${beskrivelse}</p>
        <p><strong>Trinn:</strong> ${trinn}</p>
    `;
    visittkortDiv.classList.add('vis'); // Legg til klassen 'vis' for å vise visittkortet
    visittkortDiv.style.backgroundColor = farge; // Oppdater bakgrunnsfargen til visittkortet
}

function endreFarge() {
    const farge = document.getElementById("farge").value;
    const visittkortDiv = document.getElementById('visittkort');
    visittkortDiv.style.backgroundColor = farge; // Oppdater bakgrunnsfargen til visittkortet
}