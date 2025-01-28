function genererVisittkort() {
    const navn = document.getElementById('navn').value;
    const telefon = document.getElementById('telefon').value;
    const beskrivelse = document.getElementById('beskrivelse').value;
    const trinn = document.getElementById('trinn').value;

    const visittkortDiv = document.getElementById('visittkort');
    visittkortDiv.innerHTML = `
        <h2>Visittkort</h2>
        <p><strong>Navn:</strong> ${navn}</p>
        <p><strong>Telefonnummer:</strong> ${telefon}</p>
        <p><strong>Om personen:</strong> ${beskrivelse}</p>
        <p><strong>Trinn:</strong> ${trinn}</p>
    `;
    visittkortDiv.classList.add('vis'); // Legg til klassen 'vis' for å vise visittkortet
}