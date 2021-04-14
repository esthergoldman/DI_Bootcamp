

//declaring

function familyAge(myAge){
   let ageMum = myAge*2
   let ageDad = ageMum*1.2
   console.log(`The age of my mum is ${ageMum}, the age of my dad is ${ageDad}`)
}


//invoke
familyAge(60)


//////////-------------------------------------------

 ////GLOBAL VARIABLE
 //DECLARED IN THE GLOBAL SCOPE
 let username="lea" //global scope, global dont access local
console.log("username")

// local and global are differente enviroment
//declaring
function familyAge(myAge){
    //these are local varibales ageMum ageDad,local can acces global
    let ageMum = myAge*2
    let ageDad = ageMum*1.2
    console.log(`The age of my mum is ${ageMum}, the age of my dad is ${ageDad}`)
 }
 
 
 //invoke
 familyAge(60)
 ///global scope
 //undefined
 console.log(ageMum)

 //LOCAL VARIABLE IS A VARIABLE DECLARED IN THE LOCAL SCOPE
 // YOUCANNOT ACCESS A LOCAL VARIABLE IN THE LOCAL SCOPE




 /////////////---------------------------------
//RETURN

//1st function calculate age of dad 
 function familyAge(myAge){ //function  //4step
     let ageDad = myAge*1.2 //40
     return ageDad // 5fth step // return asign a result to the function
    ///dont console.log after the return, nothing after return, it wont get executed
 }

 //OUTSIDE FUNCTION CREATE VARIABLE
// second function display the details about the dad
function familyDetail(){  //2
    //dadDetail = ageDad = 40
    let dadDetail = familyAge(20)  //3  //6
    console.log (`My dad is ${dadDetail}`)
}
 familyDetail() //1









////////////////////////////// no se q es o donde iba
/* 

 let retrieveAgeDad = FamilyAge(20) 
 //let retrieveAgeDad = FamilyAge(20) = ageDad = myAge*1.2 =number
console.log(`retrieveAgeDad is ${retrieveAgeDad}`)
 //RETURN VALUE
 ////--->GIVING A RESULT TO THE FUNCTION
 ///FUNCTION = RETURNED VALUE */