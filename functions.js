
//1
const helloWorld = () => "Hello World";


//2
const helloName = (name) => `Hello ${name}`;


//3
const square = (number) => number ** 2;


//4
const area = (side1, side2) => side1 * side2;


//5
const circleInfo = (radius) => [2 * Math.PI * radius, Math.PI * (radius ** 2)];


//6
const vowelCount = (string) => {
    const regex = /[aAeEiIoOuU]/g;
    return string.match(regex).length;
}


//7
const arrayLengthMatch = (arr1, arr2) => arr1.length === arr2.length;


//8 
const numberToArray = (numbers) => {
    let func = (num) => Number(num);
    return Array.from(String(numbers), func);
}



//9 
const getTruthyFalsyArr = (arr) => {
    const myArray = [];
    for (let value of arr){
        if(value){
            myArray.push(true);
            continue;
        }
        myArray.push(false);
    }
    return myArray;
}