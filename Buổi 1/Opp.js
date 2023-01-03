function Animals(name,height) {
    let newAnimal = Object.create(animalConstructor);
    newAnimal.name = name;
    newAnimal.height = height;
    return newAnimal;
}
let animalConstructor = {
    meat: function() {
        return `${this.name} eat meat`;
    },
    vegetable: function() {
        return `${this.name} eat vegetable`;
    },
    animalHeight: function() {
        return `He tail ${this.height} m`;
    }
}

function Lions(name,height,speedRun) {
    let newLion = Animals(name,height);
    Object.setPrototypeOf(newLion,lionConstructor);
    newLion.speedRun =speedRun ;
    return newLion;
}
let lionConstructor = {
    speedRuns() {
        return `He is speed run ${this.speedRun} Km/h`;
    }
    
}
function Birds(name,height,speedFly) {
    let newBirds = Animals(name,height);
    Object.setPrototypeOf(newBirds,birdConstructor);
    newBirds.speedFly =speedFly;
    return newBirds;
}
let birdConstructor = {
    speedFlys() {
        return `She is can fly ${this.speedFly} Km/h`;
    }
}

Object.setPrototypeOf(lionConstructor ,animalConstructor,birdConstructor);
const lion = Lions("Goku","201", "200");
const bird=Birds("Clara","225","292");
console.log(lion.meat() +" "+ lion.animalHeight() +" and "+lion.speedRuns());
// console.log(bird.vegetable + bird.animalHeight+" and "+bird.speedFlys());