
//exercise 1

var x= 5;
var y= 1;

if (x>=2) {
    console.log("x is the biggest number")
}



//exercise 3

var number = Number(prompt("Enter a number"));

//if the remainder value is 0 then it is an even number
//we are using % modulus operator to get the remainder value
if ( number % 2 == 0) {
	alert('x is an even Number');
}else{
	alert('x is not an even number');
}


//exercise 2
var newDog = "Chihuahua";
var n = newDog.length;
console.log(n)
console.log(newDog.toUpperCase);
console.log(newDog.toLowerCase);

if ( newDog  == "Chihuahua") {
	alert('I love Chihuahua, it’s my favorite dog breed');
}else{
	alert('I dont care, I prefer cat');
}


//exercise 4

let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"]
    let nu= users.length;
    let nr= nu-2;
console.log(nu);
//no one is online
if ( users.length  == 0 ) {
	console.log("no one is online");
}

//1 person online
else if ( users.length  == 1 ) {
    console.log("one person is online");}

//2 people online
else if ( users.length  == 2 ) {
	console.log('<name_user1> and <name_user2> are online');
}

// n>2 online
else if ( users.length > 2 ) {
	console.log (users[0] + users[1] + 'and' + nr + 'more are online');
}

