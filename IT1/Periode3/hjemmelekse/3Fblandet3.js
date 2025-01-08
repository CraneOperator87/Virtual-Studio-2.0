let figur1 = {
    form: "rektangel",
    lengde: 4,
    bredde: 6,
    areal: 24,
    omkrets: 20,

    skrivUtEgenskaper() {
        console.log(Object.keys(this));
    },

    skrivUtEgenskaperOgVerdier() {
        for (let key in this) {
            if (this.hasOwnProperty(key)) {
                console.log(`${key}: ${this[key]}`);
            }
        }
    },

    antallEgenskaper() {
        return Object.keys(this).length;
    }
};

// Test metodene
figur1.skrivUtEgenskaper();
figur1.skrivUtEgenskaperOgVerdier();
console.log(`Antall egenskaper: ${figur1.antallEgenskaper()}`);

// ^^^ Koden skriver ut metodene og jeg vet ikke helt hvordan jeg skal løse det. ^^^

let figur2 = {
    form: "rektangel",
    lengde: 4,
    bredde: 6,
    areal: 24,
    omkrets: 20
};
  
let figur3 = {
    form: "rektangel",
    lengde: 9,
    bredde: 1,
    omkrets: 20
};
  
let figur4 = {
    form: "kvadrat",
    lengde: 4,
    bredde: 4,
    areal: 16
};
  
let figur5 = {
    form: "kvadrat",
    lengde: 6,
    bredde: 6
};

// Funksjon for å sammenligne to objekter
function erLike(obj1, obj2) {   //filter funksjonen og resten er hentet av AI. Jeg klarte ikke å løse det uten.
    let keys1 = Object.keys(obj1).filter(key => typeof obj1[key] !== 'function');
    let keys2 = Object.keys(obj2).filter(key => typeof obj2[key] !== 'function');
                                
    if (keys1.length !== keys2.length) {
        return false;
    }

    for (let key of keys1) {
        if (!obj2.hasOwnProperty(key) || obj1[key] !== obj2[key]) {
            return false;
        }
    }

    return true;
}

console.log(erLike(figur1, figur2)); // true
console.log(erLike(figur1, figur3)); // false
console.log(erLike(figur1, figur4)); // false
console.log(erLike(figur1, figur5)); // false
console.log(erLike(figur4, figur5)); // false


// Oppgave b er litt for komplisert for meg.