// FØR spillet starter:
let startSpillE1 = document.querySelector("#spillStart"); // den grønne knappen
startSpillE1.addEventListener("click", startSpillet);     // funksjon start spill

let restartSpillE1 = document.querySelector("#restart");  // starte spillet på nytt
restartSpillE1.addEventListener("click", restartSpillet); // funksjon restart spill 

let spillStateE1 = document.querySelector("#spillState");     // Startet eller ikke
let spillContentE1 = document.querySelector("#spillInnhold"); // Dette viser hele innholdet.

// under spillet, kun elementer fra html vi kobler sammen 
let kastTerningButtons = document.querySelectorAll("#kastTerning"); // querrtSelectorAll hentet fra w3Schools
let terningResultat1E1 = document.querySelector("#terningResultat1");
let terningResultat2E1 = document.querySelector("#terningResultat2");

// Spiller 1
let spiller1ScoreE1 = document.querySelector("#spiller1");
let spiller1Score = 0;
let poengSum1 = 0;
let poengSum1E1 = document.querySelector("#poengSum1");

// Spiller 2
let spiller2ScoreE1 = document.querySelector("#spiller2");
let spiller2Score = 0;
let poengSum2 = 0;
let poengSum2E1 = document.querySelector("#poengSum2");

let currentSpiller = 1;

// Denne delen hentet også fra w3Schools:
kastTerningButtons.forEach((button, index) => {
    button.addEventListener("click", () => kastTerning(index + 1));
});

// Denne funksjonen vet jeg nøyaktig hva den gjør, og har skrevet selv før, men trengte litt hjelp fra youtube tutorial:
function startSpillet() {
    console.log("Spillet har startet");
    startSpillE1.style.display = "none";
    spillContentE1.style.display = "block"; 
    spillStateE1.textContent = "Spillet har startet!";
    updateButtonStates();
}

function kastTerning(spiller) {
    let terningResultat = Math.floor(Math.random() * 6) + 1;
    let spillerScoreE1, terningResultatE1, spillerScore, poengSumE1, poengSum;

    if (spiller === 1) {
        spillerScoreE1 = spiller1ScoreE1;
        terningResultatE1 = terningResultat1E1;
        spillerScore = spiller1Score;
        poengSumE1 = poengSum1E1;
        poengSum = poengSum1;

        spillStateE1.textContent = "Spillet pågår!";

    } else {
        spillerScoreE1 = spiller2ScoreE1;
        terningResultatE1 = terningResultat2E1;
        spillerScore = spiller2Score;
        poengSumE1 = poengSum2E1;
        poengSum = poengSum2;
        spillStateE1.textContent = "Spillet pågår!";

    }

    spillerScore += terningResultat;
    if (spillerScore > 50) {
        spillerScore = 50 - (spillerScore - 50);
    }
    // Hjelp fra AI:
    terningResultatE1.textContent = `Resultat av kast: ${terningResultat}`;
    spillerScoreE1.textContent = `Spiller ${spiller}: ${spillerScore}`;

    if (spillerScore === 50) {
        poengSum++;
        poengSumE1.textContent = `Poengsum Spiller ${spiller}: ${poengSum}`;
        spillerScore = 0;
    }

    if (spiller === 1) {
        spiller1Score = spillerScore;
        poengSum1 = poengSum;
    } else {
        spiller2Score = spillerScore;
        poengSum2 = poengSum;
    }

    // Henta fra AI:
    currentSpiller = currentSpiller === 1 ? 2 : 1;
    updateButtonStates();
}

// Hele funksjon hentet fra w3Schools:
function updateButtonStates() {
    kastTerningButtons.forEach((button, index) => {
        if (index + 1 === currentSpiller) {
            button.disabled = false;
            button.style.backgroundColor = "#919792";
            button.style.cursor = "pointer";
        } else {
            button.disabled = true;
            button.style.backgroundColor = "red";
            button.style.cursor = "not-allowed";
        }
    });
}

function restartSpillet() {
    spiller1Score = 0;
    spiller2Score = 0;
    poengSum1 = 0;
    poengSum2 = 0;
    currentSpiller = 1;

    spiller1ScoreE1.textContent = "Spiller 1: 0";
    spiller2ScoreE1.textContent = "Spiller 2: 0";
    poengSum1E1.textContent = "Poengsum Spiller 1: 0";
    poengSum2E1.textContent = "Poengsum Spiller 2: 0";
    terningResultat1E1.textContent = "0";
    terningResultat2E1.textContent = "0";

    spillStateE1.textContent = "Spillet har restarta!";


    updateButtonStates();
}