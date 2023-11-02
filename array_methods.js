//1 array.at could get -1 as an input and return the last number in the array, and arr.at as a new feature and could be not supported on all browsers.

//2
const arrayLengthMultiply = (char, number) => {
    return [...Array(number)].fill(char);
}

//3
const arrayNRemover = (arr, n) => {
    if (n > arr.length || n < 0){
        return "Error";
    } else {
        return arr.slice(0, arr.length - n);
    }
}

//4
const arrayShifter = (arr, num) => {
    arr.unshift(num);
}

//5
const arrayConnector = (arr1, arr2) => {
    let arr = [];
    arr = arr.concat(arr1).concat(arr2);
    return arr;
}

//6
const arrayUpperCaser = (arr) => {
    return arr.map((x) => x.toUpperCase());
}

//7 
const evenArray = (arr) => {
    return arr.filter((number) => (number / 10) >= 1)
}

//8 
const isInArray = (arr, parameter) => {
    return arr.includes(parameter);
}

//9 
const biggerThenTenIndex = (arr) => {
    return arr.find((number) => number > 10);
}

//10 
const isBiggerThenTenIndex = (arr) => {
    index = biggerThenTenIndex(arr);
    if(index !== undefined){
        return true;
    }
    return false;
}

//11 sort by default preforms string based filtering so it try's to preform alphabetic sorting on numbers which works by indicating the first letter.
// const array1 = [1, 30, 4, 21, 100000];
// console.log(array1.sort());

//12
const sortByNumbers = (arr) => {
    return arr.sort((a, b) => a - b);
}

//13 
const starsSort = (arr) => {
    return sortByNumbers(arr).join('**');
} 

//14 
const alphabeticSort = (arr) => {
    return arr.sort();
}

//15
const isTargetValid = (arr, target) => {
    const arrCopy = arr.filter((number) => number < target)
    if(arrCopy.length === arr.length){
        return true;
    } 
    return false;
}  

//16
const helpingFunction = (target, number) => {
    if(number > target){
        return true;
    }
    return false;
}

const mainFunction = (target, arr) => {
    const iterator1 = arr[Symbol.iterator]();

    for (const value of iterator1) {
        if(helpingFunction(target, value)){
            return true;
        }
    }

    return false;
}
