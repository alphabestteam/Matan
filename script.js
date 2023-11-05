function addEvent(counterDisplay) {
    let counter = 0;

    function countAdder() {
        counter++;
        counterDisplay.textContent = counter;
    }
    return countAdder;
}


const button = document.getElementById("my-button");
const counterDisplay = document.getElementById("counter-display");
button.addEventListener("click", addEvent(counterDisplay));