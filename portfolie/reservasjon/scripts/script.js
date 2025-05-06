console.log("Script Lastet inn.");

document.querySelector("#reservasjon").addEventListener("click", resCon);

document.querySelector("#gjester").addEventListener("input", function() {
    document.querySelector("#antallGjester").textContent = `Antall gjester: ${this.value}`;
});

function resCon() {
    const navn = document.querySelector('#navn').value;
    const telefon = document.querySelector('#telefon').value;
    const dato = document.querySelector('#dato').value;
    const tid = document.querySelector('#ledigereservasjoner').value;
    const gjester = document.querySelector('#gjester').value;

    //Kobler opp til elementer
    const resDivE1 = document.querySelector('#resDiv');
    const regSkjemaE1 = document.querySelector('#regskjema');

    // Dette er REN hjelp fra nettside, jeg mener dette er en liten kul itilegg til koden :)
    if (!navn || !telefon || !dato) {
        alert("Vennligst fyll ut alle feltene før du reserverer.");
        return;
    }

    ///
    /// if (ledigereservasjoner === "18:30" || "19:00" || "19:30" || "20:00" || "20:30") {
    ///    alert("Dette tidspunktet er dessverre fullbooket. Vennligst velg et annet tidspunkt.");
    ///     return;

    /// }
    
    regSkjemaE1.style.display = "none"; // Skjul skjemaet

    // Vis bekreftelsesmelding
    resDivE1.innerHTML = `
        <h2>Din reservasjon er mottatt!</h2>
        <p><strong>Navn under reservasjonen:</strong> ${navn}</p>
        <p><strong>Registrert telefonnummer:</strong> ${telefon}</p>
        <p><strong>Dato reservert:</strong> ${dato}</p>
        <p><strong>Tidspunkt:</strong> ${tid}</p>
        <p><strong>Antall gjester:</strong> ${gjester}</p>
        <p>Vi gleder oss til å se deg!</p>
    `;
    resDivE1.style.display = "block"; // Vis bekreftelsesmeldingen
}
