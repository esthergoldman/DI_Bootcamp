//retrieve the element
let paragraph = document.getElementById("p")
paragraph.addEventListener("click",clickMe2) //clickMe function

//retrieve the element
let listShopping =  document.getElementById("list")
listShopping.addEventListener("click",clickMe)

function clickMe(event){ //event refers to element clicked
	console.log("event : ", event) // ?????
	//event.target retrives the element that was clicked
	//the paragraph
	event.target.style.backgroundColor = "yellow"
}



//the function that create color after clicked
function clickMe2(event){ //event refers to element clicked
	console.log("event : ", event) // ?????
	//event.target retrives the element that was clicked
	//the paragraph
	event.target.style.backgroundColor = "red"
}