function findSeashellIndicies(target, arr) {
    /*this function finds a pair in the array that sums into 
    the target number it returns the indexes in an array*/ 
    for (let i = 0; i < arr.length - 1; i++) {
      let number_to_find = target - arr[i];
      let maybeIndex = arr.indexOf(number_to_find);
  
      if (maybeIndex !== -1) { 
        return [i, maybeIndex];
      }
    }
    return null;
  }

console.log(findSeashellIndicies(30, [5, 10, 15, 21, 25]))