
//Definere variabler

let x = 5;
let y = 5;

console.log(typeof x);


// for løkke
for (let i =0; i< 5; i++) { // i++ = i = i + 1
    console.log(i);
}

// while løkke
let antall = 0;

while (antall < 5) { 
    console.log(antall);
    antall++;
}

// funksjoner

function hilsen(navn) {
    return "Hei " + navn;
}

// kaller funksjonen
console.log(hilsen("Per"));

// Lambda funksjon
const leggTil = (a, b) => a + b;

// Bruk av lambda funksjon
let resultat = leggTil(5, 5);
console.log(resultat);

// Streng

let navn = "Per";
let alder = 25;

console.log(`Hei ${navn}, du er ${alder} år gammel`);

