document.addEventListener("DOMContentLoaded", function () {
    const textHtml = document.getElementById("text");

    function gradeCalculator(grade){
        if (!isNaN(grade)) {
            const numberGrade = parseInt(grade);
            let charGrade = "";
            let text = "";
    
            if (numberGrade === 100){
                charGrade = "A+";
            } 
            else if (numberGrade >= 90 && numberGrade <= 99){
                charGrade = "A";
            }
            else if (numberGrade >= 80 && numberGrade <= 89){
                charGrade = "B";
            }
            else if (numberGrade >= 70 && numberGrade <= 79){
                charGrade = "C";
            }
            else if (numberGrade >= 60 && numberGrade <= 69){
                charGrade = "D";
            }
            else if (numberGrade >= 50 && numberGrade <= 59){
                charGrade = "E";
            } 
            else if (numberGrade <= 49 && numberGrade >= 0){
                charGrade = "F";
            }
            else{
                charGrade = "Not Valid";
            }
    
            switch(charGrade){
                case "A+":
                    text = "Perfect!";
                    break;
    
                case "A":
                    text = "Amazing!";
                    break;
    
                case "B":
                    text = "Nicely done!";
                    break;
    
                case "C":
                    text = "This is fine!";
                    break;
    
                case "D":
                    text = "You can do better!";
                    break;
    
                case "E":
                    text = "Moed B is an option!";
                    break;
    
                case "F":
                    text = "Moed B is a must!";
                    break;
    
                default:
                    text = "Grade is not in the valid range!";
            }
    
            textHtml.textContent = `The grade is ${charGrade}, ${text}`;
        }
        else {
            textHtml.textContent = "Grade is not a number!";
        }
    }
    
    document.getElementById("submit").onclick = function () {
        const grade = document.getElementById("grade").value;
        gradeCalculator(grade);
    };
});
