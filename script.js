const speciesPoints = {
    'pink spotted': 4,
    'blue stinger': 3,
    'green itches': 2
};

const jellyfishDays = [
    [
        { color: 'pink'},
        { color: 'pink'},
        { color: 'blue'},
        { color: 'green'},
        { color: 'white'},
        { color: 'white'},
    ],
    [
        { color: 'pink'},
        { color: 'pink'},
        { color: 'blue'},
        { color: 'green'},
        { color: 'green'},
        { color: 'green'},
    ],
    [
        { color: 'pink'},
        { color: 'pink'},
        { color: 'pink'},
        { color: 'pink'},
        { color: 'blue'},
        { color: 'green'},
    ]
];

let score = 0;

// SpongeBob's net callback function
function catchJellyfish(jellyfish, identifyJellyfishAndAddPoints) {
    console.log(`spongebob caught a ${jellyfish.color} jellyfish!`);
    identifyJellyfishAndAddPoints(jellyfish, addPoints);
}

// Patrick's net callback function
function identifyJellyfishAndAddPoints(jellyfish, addPoints) {
    const specie = identifySpecies(jellyfish.color);
    console.log(`Patrick identified a ${specie} jellyfish!`);
    addPoints(specie)
}

// Score keeping callback function
function addPoints(species) {
    if (speciesPoints[species] === undefined){
        score += 1;
    } else {
    score += speciesPoints[species];
    }

    console.log(`score: ${score}`);
}

// Helper functions
function identifySpecies(color) {
    for (let specie in speciesPoints) {
        if (color === specie.split(' ')[0]) {
            return specie;
        }
    }
    return "common";
}

//The Adventure Starts Here! 
for (const day of jellyfishDays){
    console.log("Let's go jellyfishing!");

    for (const jellyfish of day){
        catchJellyfish(jellyfish, identifyJellyfishAndAddPoints);
    }

    console.log(`Great job, Spongebob and Patrick!
                 final score: 15`);
    score = 0;
}