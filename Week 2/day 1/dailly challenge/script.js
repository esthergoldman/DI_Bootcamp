let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
fruits.shift();
console.log(fruits);

fruits.sort();
console.log(fruits);

fruits.push("kiwi");
console.log(fruits);

delete fruits[0];
console.log(fruits);

let reversed= fruits.reverse();
console.log("reversed:", reversed);

//part2

let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
console.log(moreFruits[1][1][0]);