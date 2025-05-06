function bubbleSort(arr) {
    for (let i = 0; i < arr.length - 1; i++) {
        for (let j = 0; j < arr.length - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                // Bytt plass på arr[j] og arr[j + 1]
                let temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
    return arr;
}

// Eksempel på bruk:
let tall = [5, 2, 9, 1, 7];
let sortert = bubbleSort(tall);
console.log(sortert); // Output: [1, 2, 5, 7, 9]
