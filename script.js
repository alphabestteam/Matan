function sequenceA() {
    setTimeout(_ => console.log('Sponge'), 0);
    console.log("Bob");
}

function sequenceB(){
    setTimeout(_ => console.log(`🍅 Timeout at B`), 0);
    Promise.resolve().then(_ => console.log('🍍 Promise at B'));
}

function sequenceC(){
    setTimeout(_ => console.log(`🍅 Timeout at C`), 0);
    Promise.resolve().then(_ => setTimeout(console.log('🍍 Promise at C'), 1000));
}

function sequenceD(){
    console.log('Sponge');
    setTimeout(_ => console.log('Square'), 0);
    Promise.resolve().then(_ => console.log('Pants'));
    console.log('Bob');
}

function questionA(){
    sequenceA();
}

function questionB(){
    sequenceB();
}

function questionC(){
    sequenceC();
}

function questionD(){
    sequenceD();
}

function questionE(){
    sequenceB();
    sequenceC();
}

//questionA();
//Bob will print first because timeout with 0 will set to be in the next event loop so bob will print first.

// questionB();
//Promise is task with higher priority then other other event loop tasks so it will print first.

// questionC();
// promise is resolved in the microtask queue and then when main thread is available the timeout function will work.

// questionD();
//sponge and bob will print first because is a synchronous then pants because of the promise then timeout.

// questionE();
//it will do promise bb first because it has the lowest timeout and then promise c , then timeout b and c, b will be first because its first function called.