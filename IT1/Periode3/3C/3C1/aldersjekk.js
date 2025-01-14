let alder = 19;

// alder er 13 eller høyere OG mindre enn 19
if (alder >= 13 && alder <= 19) { // && -> [13, 19]
    console.log("Du er en tenåring");
} else if (alder < 13) {
    console.log("Du er et barn");
} else {
    console.log("Du er en voksen");
}

// && betyr "og"

if (alder < 13 || alder > 19) { // || ->  < <- , 13 > u < 19 , -> >
    console.log("Du er ikke en tenåring");
}

console.log(!true);  // skriver ut false
console.log(!false); // skriver ut true