const myMap = new Map([
    ['Main character', 'spongebob'],
    ['Best friend', 'patrick'],
    ['pet', 'gary'],
    ['word buddy', 'squidward'],
    ['manager', 'Mr. Krabs'],
    ['teacher', 'Mrs. Puff'],
    ['location', 'bikini bottom']
]);

//1
for (const [key, value] of myMap) {
  console.log(`${key}: ${value}`);
}

//2
const keysArray = Array.from(myMap.keys());
console.log(keysArray);

//3
console.log(myMap.get('location'));

//4
console.log(myMap.size);

//5
myMap.delete('location');

//6
console.log(myMap.size);

//7
for (const [key, value] of myMap) {
    console.log(`${key}: ${value}`);
}

//8
console.log(myMap.has('location'));