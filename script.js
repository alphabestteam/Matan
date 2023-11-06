const quotes = [
    "I'm ready, I'm ready, I'm ready! - SpongeBob SquarePants",
    "F is for friends who do stuff together, U is for you and me, N is for anywhere and anytime at all! - SpongeBob SquarePants",
    "I'm not just ready, I'm ready Freddy! - SpongeBob SquarePants",
    "Remember, licking doorknobs is illegal on other planets. - SpongeBob SquarePants",
    "The inner machinations of my mind are an enigma. - Patrick Star",
    "I can't hear you, it's too dark in here! - Patrick Star",
    "I'm ugly and I'm proud! - SpongeBob SquarePants",
    "I'll have you know that I stubbed my toe last week while watering my spice garden and I only cried for 20 minutes. - Squidward Tentacles",
    "Once there was an ugly barnacle. He was so ugly that everyone died. The end. - Patrick Star",
    "Is mayonnaise an instrument? - Patrick Star",
    "Can you give SpongeBob his brain back? - Patrick Star",
    "I guess hibernation is the opposite of beauty sleep. - Squidward Tentacles",
    "I know of a place where you never get harmed. A magical place with magical charms. Indoors! Indoors! Indoors! - SpongeBob SquarePants",
    "I can't believe I'm finally wearing a Krusty Krab hat. Promotion, here I come! - SpongeBob SquarePants",
    "I'll take a double triple bossy deluxe on a raft, 4x4, animal-style, extra shingles with a shimmy and a squeeze, light axle grease, make it cry, burn it, and let it swim. - Bubble Bass",
    "Sandy: What do you usually do when I'm gone? SpongeBob: Wait for you to come back.",
    "SpongeBob: Don't worry, Mr. Krabs, I'll have you out of there faster than a toupee in a hurricane!",
    "SpongeBob: I know of a place where you never get harmed. A magical place with magical charm. Indoors. Indoors. Indoors. - Squidward: What's that? - SpongeBob: Outdoors.",
    "SpongeBob: Can I be excused for the rest of my life?",
    "SpongeBob: I'm not just ready, I'm ready Freddy!",
    "SpongeBob: You don't need a license to drive a sandwich.",
    "SpongeBob: Goodbye everyone, I'll remember you all in therapy.",
    "SpongeBob: Patrick, I don't think Wumbo is a real word. Patrick: Come on, SpongeBob, we're best friends. I would never call you a Wumbologist if I didn't think you were one.",
    "SpongeBob: I'm a Goofy Goober, yeah. You're a Goofy Goober, yeah. We're all Goofy Goobers, yeah. Goofy, goofy, goober, goober, yeah!",
    "SpongeBob: Once there was an ugly barnacle. He was so ugly that everyone died. The end."
];

let charArray = [];
let running = false;
let time = 0;
let interval;
const timer = document.getElementById("timer");
const table = document.getElementById("table");


function getRandomQuote() {
    //implement getting a random quote from the array.
    const randomIndex = Math.floor(Math.random() * quotes.length);
    return quotes[randomIndex];
}


function createTable() {
    const tbody = document.getElementById("tbody")

    for (let key in localStorage) {
        if (localStorage.hasOwnProperty(key)) {
            const row = document.createElement('tr'); 
            const keyCell = document.createElement('td'); 
            keyCell.textContent = key; 
            row.appendChild(keyCell); 
            const value = localStorage.getItem(key).split(",");
            for (let val of value) {
                const valueCell = document.createElement('td'); 
                const span = document.createElement('h2'); 
                span.textContent = val; 
                valueCell.appendChild(span); 
                row.appendChild(valueCell); 
            }
            tbody.appendChild(row); 
            document.body.appendChild(table);
        }
    }
}


function sortTable() {
    const table = document.getElementById('table');
    const tbody = table.querySelector('tbody');
    const rows = Array.from(tbody.querySelectorAll('tr'));
    let counter = 1;

    rows.sort((a, b) => {
        const scoreA = parseInt(a.children[5].textContent);
        const scoreB = parseInt(b.children[5].textContent);

        return scoreB - scoreA;
    });

    while (tbody.firstChild) {
        tbody.removeChild(tbody.firstChild);
    }

    rows.forEach((row) => {
        row.children[0].textContent = counter;

        if(counter == 1){
            row.children[0].style.backgroundColor = "gold";
        }else if(counter == 2){
            row.children[0].style.backgroundColor = "silver";
        }else if(counter == 3){
            row.children[0].style.backgroundColor = "chocolate";
        }

        counter ++;
        tbody.appendChild(row);
    });
}


function startGame() {
    /*
    1 - implement game start/restart logic 
    2 - generate a random quote and display it in the relevant html element
    2* - think carefully how to do it such that you can change the background of each char individually
    */
    const quote = document.getElementById("quote");
    const randomQuote = getRandomQuote();
    charArray = [];

    if (quote.dataset.start == "false") {
        for (let char of randomQuote) {
            const element = document.createElement("span");
            element.textContent = char;
            quote.appendChild(element);
            charArray.push(element);
        }
        quote.dataset.start = "true";
    } else {
        location.reload();
    }

    startStopTimer();
}


function checkInput() {
    //implement checking input, ending the game by calling the endGame() function when needed. 
    //add the relevant css class to each letter
    const input = document.getElementById("input").value;
    const quote = document.getElementById("quote");
    const quoteChars = quote.innerText.split("");

    for (let i = 0; i < quoteChars.length; i++) {
        if (i < input.length) {
            if (input[i] === quoteChars[i]) {
                charArray[i].style.backgroundColor = "green";
            } else {
                charArray[i].style.backgroundColor = "red";
            }
        } else {
            charArray[i].style.backgroundColor = "";
        }
    }

    if (input.length === quoteChars.length) {
        endGame(input, quote.innerText);
    }
}

function countMatchingChars(strA, strB) {
    //helper function used to calculate hits, used for percentage.
    let strArr = strA.split("");
    let strBrr = strB.split("");
    let count = 0;

    for (let i = 0; i < strBrr.length; i++) {
        if (strArr[i] === strBrr[i]) {
            count++;
        }
    }
    return count;
}

//-----------------------------------------------------
function startStopTimer() {
    if (running) {
        clearInterval(interval);
    } else {
        interval = setInterval(function () {
            time++;
            updateDisplay();
        }, 1000);
    }
    running = !running;
}


function updateDisplay() {
    const minutes = Math.floor(time / 60);
    const seconds = time % 60;
    timer.textContent = minutes + ":" + (seconds < 10 ? "0" : "") + seconds;
}
//------------------------------------------------------
function endGame(input, quote) {
    //stop the timer, calculate elapsed time in seconds
    //in the result element display:
    //  a) how many words were typed
    //  b) in how many seconds it was done
    //  c) the speed (wpm)
    //  d) the accuracy as percentage
    startStopTimer();
    let greenCount = countMatchingChars(input, quote);
    let wordCount = input.split(/\s+/).length - 1;
    const resultElement = document.getElementById("result");
    resultElement.innerText = `words typed: ${wordCount}
                               Accuracy: ${Math.floor((greenCount / quote.length) * 100)}%
                               total time: ${time} seconds
                               words per minute: ${wordCount / (time / 60)}`;

    localStorage.setItem(String(localStorage.length + 1), [wordCount, time, wordCount / (time / 60), Math.floor((greenCount / quote.length) * 100), Math.floor((greenCount / quote.length) * (wordCount / (time / 60)))])
}

createTable();
sortTable();

const startButton = document.getElementById("start-btn");
startButton.addEventListener("click", startGame);

const input = document.getElementById("input");
input.addEventListener("input", checkInput);

