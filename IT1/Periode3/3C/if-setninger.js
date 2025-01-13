let riktigTall = 43;
let gjettet;
gjettet = 17;

if (gjettet === riktigTall) {
    console.log("Riktig!");
}

if (gjettet !== riktigTall) {
    console.log("Feil!");
}

// eller gjøre det i ett:

if (gjettet === riktigTall) {
    console.log("Riktig!");
} else { // <-- her legger man "else"
    console.log("Feil!");
}


//større eller lavt

if (gjettet === riktigTall) {
    console.log("Riktig!");
} else if (gjettet > riktigTall) { // <-- her elif fra python
    console.log("For lavt!");
} else {
    console.log("For høyt!");
}