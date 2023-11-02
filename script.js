const bobFriends = ['sandy', 'patrick', 'squidward', 'Mr. krabs', 'Gary'];

console.log(bobFriends);
console.log(bobFriends.length);

bobFriends.push('Mrs. puff');

console.log(bobFriends);
console.log(bobFriends.length);

bobFriends.shift();
bobFriends.unshift('Pearl');
console.log(bobFriends);

//You can to change values of an array even if its const because the const is only the address of the memory where the array is stored so you can change the values and length.