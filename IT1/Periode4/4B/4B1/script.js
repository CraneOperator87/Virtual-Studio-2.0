// finne frem overskrift-elementet og for hver gang det trykkes skal den øke med 1 //
let overskriftEl = document.querySelector("h1");
overskriftEl.addEventListener("click", skrivAntall);

// finne frem anvsnitt elementet og legge den sammen med <p> som har id farge //
let avsnittEl = document.querySelector("#farge");
avsnittEl.addEventListener("click", byttFargeText);

// finne frem kantlinje element, koble den med <p> som har id kantlinje //
let kantlinjeEl = document.querySelector("#kantlinje");
kantlinjeEl.addEventListener("click", byttFargeKantLinje);

let buttonEl = document.querySelector("#knapp");
buttonEl.addEventListener("click", skiftFarge);

// finne frem hoved //
let hovedEl = document.querySelector("#hoved");

let antallTrykk = 0;
let tur = 0;

// Oppgave 2 for å bytte farge på teksten til h1 //
function byttFargeText() {
    let farge = Math.floor(Math.random() * 365);
    overskriftEl.style.color = "hsl(" + farge + ", 100%, 50%)";
}

// Oppgave 3 for å bytte kantlinje til hoved-div//
// Her tar vi frem kantLinje, så kobler vi den sammen med hoved, og for hver gang det trykkes skal den bytte farge //
function byttFargeKantLinje () {
    let farge = Math.floor(Math.random() * 365);
    hovedEl.style.borderColor = "hsl(" + farge + ", 100%, 50%)";
}

function skiftFarge() {
    if (tur == 0) {
        let farge = Math.floor(Math.random() * 365);
        overskriftEl.style.color = "hsl(" + farge + ", 100%, 50%)";
        tur ++;
    } else {
        let farge = Math.floor(Math.random() * 365);
        hovedEl.style.borderColor = "hsl(" + farge + ", 100%, 50%)";
        tur = 0;
    }
}

// Holder tellingen //
function skrivAntall() {
    if (antallTrykk < 9) { // Oppgave 5 //
        antallTrykk++; 
        overskriftEl.innerHTML = "Du har trykket på meg " + antallTrykk + " ganger.";
    } else {
        overskriftEl.innerHTML = "Du har trykket meg 10 ganger, nå får du ikke trykke mer."; // Endrer teksten //
        overskriftEl.removeEventListener                                                     // Fjerner eventListeneren, da skjer ingenting mer //
        overskriftEl.style.cursor = "not-allowed";                                           // Endrer til at du ikke får lov å trykke //
    }


}