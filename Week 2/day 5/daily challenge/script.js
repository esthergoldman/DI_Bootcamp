 //1
   let str = 'The movie is not that bad really, I like it';
// string into array
   let res = str.split(" ");
   console.log(res)
//3
let not= s2.indexOf("not");
let bad= s2=indexOf("bad");
let wordCounts= bad-not+1


if(notIndex < badIndex){
   arraySentence.splice(notIndex,wordCounts, "good")
   console.log(arraySentence.join(" "))
}




let sentence= "the movie is not so very bad i like it"
//1sthow can i word easily?? thing conver string to arrat
let arraySentence= sentence.split (" ")
//create variable for code that i need to reuse
let notIndex= arraySentence.indexOf("not");
let badIndex= arraySentence.indexOf("bad");
//count the words between not and bad? we have a tool : indexOf
let wordCounts= badIndex-notIndex+1


// how i check that the word "not" is before the word "bad"?
if(notIndex < badIndex){
            //    startIndex, howManyElementsToDelete,ElementToAddInstead
    //how to i delete the "not"...."bad" and replace it with "good"
    arraySentence.splice(notIndex,wordCounts, "good")
    //now that i have an array, how can i display a string?
    console.log(arraySentence.join(" "))
}
 */