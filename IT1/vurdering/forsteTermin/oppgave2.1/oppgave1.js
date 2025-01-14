function isBetween(a, b, c) {
    return (a > b && a < c) || (a > c && a < b);
}

console.log(isBetween(5, 1, 10)); // true
console.log(isBetween(5, 10, 1)); // true
console.log(isBetween(1, 5, 10)); // false
console.log(isBetween(10, 1, 5)); // false