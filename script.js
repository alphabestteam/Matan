const main = document.querySelector('main');



// const naiveHead1 = createHeading('red', 'naive 1');
// const naiveHead2 = createHeading('blue', 'naive 2');

// //this is to be changed to append a header we create by using the higher order function headingFactory(color).
// main.appendChild(naiveHead1);
// main.appendChild(naiveHead2);

// function createHeading(color, text){
//     const heading = document.createElement('h1');
//     heading.setAttribute('style', 'color: ' + color);
//     heading.textContent = text;
//     return heading;
// }

function headingFactory(color){
    //implement the closure here and use it. 
    //keep in mind you return a function. think about how one should use what this function will return.
    return function (text){
        const heading = document.createElement('h1');
        heading.setAttribute('style', 'color: ' + color);    
        heading.textContent = text;
        return heading;
    }
}

const redHeading = headingFactory('red');
const blueHeading = headingFactory('blue');
const usingFactory1 = redHeading("Using Factory 1")
const usingFactory2 = blueHeading("Using Factory 2")
main.appendChild(usingFactory1);
main.appendChild(usingFactory2);

//using higher order function is useful in order to make reusable code, i can make a factory for red headings and use it multiple times.