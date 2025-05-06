let brett = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""],
];

let brettEl = document.querySelector("#spillBrett");

function lagBrett() {
    for (let rad = 0; rad < 3; rad++) {
        for (let kolonne = 0; kolonne < 3; kolonne++) {
            const celleEl = document.createElement("div");
            celleEl.classList.add("celle");
            celleEl.dataset.rad = rad;
            celleEl.dataset.kolonne = kolonne;
            celleEl.addEventListener("click", trekk);
            brettEl.appendChild(celleEl);
        }
    }
}

function trekk(event) {
    const rad = event.target.dataset.rad;
    const kolonne = event.target.dataset.kolonne;
    console.log(`Klikket på rad ${rad}, kolonne ${kolonne}`);
}

lagBrett();