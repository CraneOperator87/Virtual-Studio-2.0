// Enkelt terningkast
let tilfeldigTall = Math.random() * 6; // 0 - 6

tilfeldigTall = Math.floor(tilfeldigTall) + 1; // 1 - 6


if (tilfeldigTall === 6) {
    console.log("Du fikk en 6er!");
} else {
    console.log ("Du fikk ikke 6er!");
}