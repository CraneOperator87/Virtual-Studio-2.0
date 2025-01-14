let overskriftEl = document.querySelector("h1");
let button1 = document.querySelector("#knapp");

let antallTrykk = 0;

button1.addEventListener("click", skrivAntall);


function skrivAntall() {
  antallTrykk++;
  overskriftEl.innerHTML = "Du har trykket kanppen " + antallTrykk + " ganger.";
}