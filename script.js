function evalNumbers(num1, num2, action) {
    if (!isNaN(num1) && !isNaN(num2)) {
        if (action === "add") {
            return `Sum of ${num1} and ${num2} is ${num1 + num2}`;
        }
        else if (action === "subtract") {
            return `Difference of ${num1} and ${num2} is ${num1 - num2}`;
        }
        else if (action === "multiply") {
            return `Product of ${num1} and ${num2} is ${num1 * num2}`;
        }
        else if (action === "divide") {
            return `Division of ${num1} and ${num2} is ${num1 / num2}`;
        }
        else if (action === "modulus") {
            return `Modulus of ${num1} and ${num2} is ${num1 % num2}`;
        }
        else {
            return "action not supported";
        }
    }
    else {
        return `${num1} or ${num2} is not a number!`;
    }
}

// console.log(evalNumbers(5,3,"add"));
// console.log(evalNumbers(5,3,"subtract"));
// console.log(evalNumbers(5,3,"multiply"));
// console.log(evalNumbers(5,3,"divide"));
// console.log(evalNumbers(5,3,"modulus"));
// console.log(evalNumbers(5,3,"sf"));
// console.log(evalNumbers("t",3,"add"));