//«Du fikk 6 eller mindre.»
//«Du fikk mellom 6 og 18.»
//«Du fikk 18 eller mer.»
//«Du fikk 13!»

let tilfeldigTall = Math.random() * 12; // 0 - 19

tilfeldigTall = Math.floor(tilfeldigTall) + 1; // 1 - 19

if (tilfeldigTall <= 6) {
    console.log("Du fikk 6 eller mindre.","(",tilfeldigTall,")")

} else if (tilfeldigTall === 13) {
    console.log("Du fikk 13.","(",tilfeldigTall,")")

} else if (tilfeldigTall >= 6 && tilfeldigTall <= 18) {
    console.log("Du fikk mellom 6 og 18.","(",tilfeldigTall,")")

} else {
    console.log("Du fikk mer enn 18.","(",tilfeldigTall,")")
}
