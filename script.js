const button = document.getElementById('the-button');
const main = document.querySelector("main");
const bobGif = document.getElementById("bob");

const toggleBob = function(){
    // Implement this function
    const count = parseInt(button.dataset.count);

    if (count % 2 !== 0) {
        bobGif.style.display = 'none';
        button.innerText = "Show me Bob ;)";
    } else {
        bobGif.style.display = 'block';
        button.innerText = "Hide Bob ;)";
    }
    button.dataset.count = count + 1;
};

bobGif.style.display = 'none';
button.innerText = "Show me Bob ;)";

button.addEventListener("click", toggleBob);
