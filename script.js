let str = ` Kung Fu Panda is a beloved animated movie about a clumsy,
food-loving panda named Po who dreams of becoming a kung fu master.\nPo's
dream becomes a reality when he is unexpectedly chosen to become the
Dragon Warrior and train with the Furious Five to protect the Valley of
Peace from the evil Tai Lung.\nKung Fu Panda was released on June 6, 2008,
and grossed over $631 million worldwide, making it the highest-grossing
non-sequel animated film at the time of its release.\nAlong the way, Po
learns valuable lessons about inner strength, perseverance, and the
importance of family and friendship.\nWith stunning animation, a
heartwarming story, and a star-studded cast including Jack Black, Angelina
Jolie, and Jackie Chan, Kung Fu Panda has become a timeless classic for
all ages. `

//1
const paragraphArray = (str) => {
    return str.split(',');
}

//2
const movieFilm = (str) => {
    return str.replace('movie', 'film');
}

//3
const allPandaBear = (str) => {
    return str.replaceAll('Panda', 'Bear');
}

//4
let str1 = str.toUpperCase();

//5 
str1 = str.toLowerCase();

//6
const firstIndex = str.indexOf('Po');

//7
// console.log(str.slice(firstIndex));

//8 
// console.log(str.trim());

//9
const slicedSubstring = str.slice(firstIndex);
const endIndex = firstIndex + slicedSubstring.indexOf('.');
console.log(str.slice(firstIndex, endIndex));

//10
const strToArray = (str) => {
    let str1 =  str.trim();
    return str1.split(' ');
}

//11
const endsWithAges = (str) => {
    return str.endsWith('ages. ');
}

//12
str = str.concat('is one of my favorite movies!');
