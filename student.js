

const vowelCount = (string) => {
    const regex = /[aAeEiIoOuU]/g;
    return string.match(regex).length;
}


function gradeAvr(arr) {
    let sum = 0;
    for (let grade of arr) {
      sum += grade;
    }
  
    return sum / arr.length;
  }


const student1 = {
    name: "matan",
    age: 19,
    grades: [50, 98, 95, 90, 50],
    average: function() {
        return gradeAvr(this.grades) + vowelCount(this.name)
    }
};


const student2 = {
    name: "Alice",
    age: 20,
    grades: [75, 88, 92, 79, 68],
    average: function() {
        return gradeAvr(this.grades) + vowelCount(this.name)
    }
};

const student3 = {
    name: "Charlie",
    age: 17,
    grades: [93, 87, 95, 74, 81],
    average: function() {
        return gradeAvr(this.grades) + vowelCount(this.name)
    }
};

const student4 = {
    name: "Frank",
    age: 23,
    grades: [62, 71, 98, 86, 53],
    average: function() {
        return gradeAvr(this.grades) + vowelCount(this.name)
    }
};

const student5 = {
    name: "Jack",
    age: 18,
    grades: [85, 90, 77, 68, 92],
    average: function() {
        return gradeAvr(this.grades) + vowelCount(this.name)
    }
};


const students = [student1, student2, student3, student4, student5];


for (let i = 0; i < students.length; i++){
    console.log(`index: ${i}`);
    console.log(`name: ${students[i].name}, age: ${students[i].age}, grades: ${students[i].grades}, average: ${students[i].average()}`);
}


const adults = students.filter((student) => student.age >= 18);
console.log(adults);