// OBJECTS : access the element by the property
let user = {
	username : "John",
	password : 1234,
	email : "john@gmail.com",
	logIn : true,
	countries : ["israel", "usa"],
	friends : {
		name : ["David", "Sarah"]
	}
}
​
console.log(user)
// 1. display the friends nested object
​let user= user[friends];
console.log(user["friends"]);

// 2. display the list of names of his friends
console.log(user["friends"]["names"]);

// 3. display the name of best friend : David

console.log(user["friends"]["names"][0]);



//second exercise

// ARRAY OF OBJECTS
let users = [
	{
		username : "John",
		password: 1234
	},
	{
		username : "Lea",
		password: 2222
	},
	{
		username : "David",
		password: 6767
	}
];
​
console.log(users)
// 1. display the information of the 2nd user (object)
console.log(users[1] );



// 2. display the password of the 2nd user
console.log(users[1]["password"]);



//conditionals:

if(condition) {
	//statement
}


if(i had money){
	i will buy a car
}




let bankAmount = 1000;

if (banckAmount) >=500){
	//if the condition is true
	consle.log("i can buy a computer")

}


//exercise 1 necesito terminarlo 

let person =29;

if (person) {
	Statement(s) to be executed if expression is true
 }
 
 let age = 18

    if (age >= 18) {
        console.log("Sorry, you are too young to drive this car.Powering off")
    }






	//switch case
	let fruit = 'Papayas';

	switch (fruit) {
	  case 'Oranges':
		console.log('Oranges are $0.59 a pound.');
		break;
	  case 'Mangoes':
	  case 'Papayas':
		console.log('Mangoes and papayas are $2.79 a pound.');
		// expected output: "Mangoes and papayas are $2.79 a pound."
		break;
	  default:
		console.log('Sorry, we are out of ' + fruit + '.');
	}

console.log("after the switch")  
//la consola te va a mostrar la segunda opcion pq tiene papaya




//excercise 2


let a = 2 + 2;

switch (a) {
  case 3:
	  // IF  a===3,respond with: "too small"
    alert( 'Too small' );
    break; 
  case 4:
	  //IF a ==4, respond with: "exactly"
    alert( 'Exactly!' );
    break; 
  case 5:
	  //if a===5, respond with:"too large"
    alert( 'Too large' );
    break;
  default:
    alert( "I don't know such values" );
}



//excercise 3
let a = 2 + 2;

switch (a) {
  case 4:
	  //IF a===4, respond with: "right"
    alert('Right!');
    break;

  case 3: // (*) grouped two cases
  case 5:
	  //IF a===5, respond with:"wrong"
    alert('Wrong!');
    alert("Why don't you take a math class?");
    break;

  default:
    alert('The result is strange. Really.');
}