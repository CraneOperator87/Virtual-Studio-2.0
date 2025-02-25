console.log("Script Lastet inn.");

document.getElementById("reservasjon").addEventListener("click", resCon);

function resCon() {
    const navn = document.getElementById('navn').value;
    const telefon = document.getElementById('telefon').value;
    const dato = document.getElementById('dato').value;
    const tid = document.getElementById('ledigereservasjoner').value;
    const gjester = document.getElementById('gjester').value;

    const resDiv = document.getElementById('resDiv');
    
    resDiv.innerHTML = `
        <h2>Din reservasjon er mottatt!</h2>
        <p><strong>Navn under reservasjonen:</strong> ${navn}</p>
        <p><strong>Registrert telefonnummer:</strong> ${telefon}</p>
        <p><strong>Dato reservert:</strong> ${dato}</p>
        <p><strong>Tidspunkt:</strong> ${tid}</p>
        <p><strong>Antall gjester:</strong> ${gjester}</p>
    `;
    resDiv.classList.remove("hidden");

    // Hide the form
    document.getElementById('regskjema').classList.add('hidden');
}