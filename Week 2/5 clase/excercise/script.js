

let arr = [];  //we want to store in the array
function my_f(sign){
    //instrucciones, funciones sirven para repetir
   
    arr.push(sign);  //everytime we press a button, stores in the array
    console.log(arr);
    let str = arr.join('');  

}

function calculate(){
    let str= arr.join('');
    console.log(str);
    let calc= eval(str);
    console.log(calc);

}

function reset(){
    arr= []; //make an empty array, we clear the data from the array
}