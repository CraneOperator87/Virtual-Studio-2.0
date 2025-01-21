let startSpillE1 = document.querySelector("#spillStart");
startSpillE1.addEventListener("click", startSpillet);

let spillContentE1 = document.querySelector("#spillInnhold");
let kastTerningButtons = document.querySelectorAll("#kastTerning");
let spiller1ScoreE1 = document.querySelector("#spiller1");
let spiller2ScoreE1 = document.querySelector("#spiller2");
let terningResultat1E1 = document.querySelector("#terningResultat1");
let terningResultat2E1 = document.querySelector("#terningResultat2");
let poengSum1E1 = document.querySelector("#poengSum1");
let poengSum2E1 = document.querySelector("#poengSum2");

let spiller1Score = 0;
let spiller2Score = 0;
let poengSum1 = 0;
let poengSum2 = 0;
let currentSpiller = 1;

function startSpillet() {
    console.log("Spillet har startet");
    startSpillE1.style.display = "none";
    spillContentE1.style.display = "block";
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
    } else {
        spillerScoreE1 = spiller2ScoreE1;
        terningResultatE1 = terningResultat2E1;
        spillerScore = spiller2Score;
        poengSumE1 = poengSum2E1;
        poengSum = poengSum2;
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
        if (index + 1 === currentPlayer) {
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

// Denne delen hentet også fra w3Schools:
kastTerningButtons.forEach((button, index) => {
    button.addEventListener("click", () => kastTerning(index + 1));
});