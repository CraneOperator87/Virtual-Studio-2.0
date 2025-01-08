document.addEventListener("DOMContentLoaded", () => {
    // Definerer to arrays: en for fargene og en for navnene på fargene på norsk
    const colors = ["red", "orange", "yellow", "green", "blue", "purple"];
    const colorNames = ["Rod", "Oransje", "Gul", "Gronn", "Bla", "Lilla"];

    // Oppretter et container-div som skal holde alle farge-divene
    const container = document.createElement("div");
    container.style.display = "flex"; // Bruker flexbox for å plassere divene ved siden av hverandre
    container.style.height = "100vh"; // Setter høyden til 100% av viewport-høyden : Youtube hjelp.
    container.style.width = "100vw"; // Setter bredden til 100% av viewport-bredden : Youtube hjelp.
    container.style.margin = "0"; // Fjerner margin
    container.style.padding = "0"; // Fjerner padding

    // Går gjennom fargene og navnene
    colors.forEach((color, index) => {
        // Oppretter et nytt div-element for hver farge
        const div = document.createElement("div");
        div.style.backgroundColor = color; // Setter bakgrunnsfargen
        div.style.flex = "1"; // Gjør at hver div tar opp like mye plass
        div.style.display = "flex"; // Bruker flexbox for å sentrere innholdet
        div.style.justifyContent = "center"; // Sentrerer innholdet horisontalt
        div.style.alignItems = "center"; // Sentrerer innholdet vertikalt
        div.style.color = "black"; // Setter tekstfargen til hvit
        div.innerText = colorNames[index]; // Setter teksten til navnet på fargen
        container.appendChild(div); // Legger til div-en i containeren
    });

    // Fjerner margin og padding fra body-elementet
    document.body.style.margin = "0";
    document.body.style.padding = "0";
    // Legger til containeren i body-elementet
    document.body.appendChild(container);
});

// For det meste av koden hentet jeg fra aunivers, men trengte å bruke andre hjelpemidler som youtube.