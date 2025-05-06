function bubbleSort(arr) {
    for (let i = 0; i < arr.length - 1; i++) {      
        let byttet = false    // Yttre løkke: Sjekke hvor mange ganger vi skal gjennom koden, 
        for (let j = 0; j < arr.length - 1 - i; j++) {  // Indre løkke: sammenligne elementer, bytte plass
            if (arr[j] > arr[j + 1]) {
                // Bytt plass på arr[j] og arr[j + 1]
                let temp = arr[j];     // Lage en temp verdi, gi verdien som skal byttes
                arr[j] = arr[j + 1];   // gamle verdi blir til neste verdi 
                arr[j + 1] = temp;     // neste verdi blir til gamle verdi
                console.log(arr)
                byttet = true
            }
        }
        if (byttet == false){
            break;
        }
        console.log("----")
    }
    return arr;
}

// Eksempel på bruk:
let tall = [2, 1, 4, 3];
let sortert = bubbleSort(tall);
console.log(sortert); // Output: [1, 2, 5, 7, 9]

