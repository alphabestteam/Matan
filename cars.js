

const myCar = {
    manufacture: "VW",
    model: "Polo",
    yearOfManufacture: 2021,
    carAge: function() {
        const currentYear = new Date().getFullYear();
        return currentYear - this.yearOfManufacture;
    }
};

console.log(`manufacture: ${myCar.manufacture},
             model: ${myCar.model},
             yearOfManufacture: ${myCar.yearOfManufacture},
             carAge: ${myCar.carAge()}`);