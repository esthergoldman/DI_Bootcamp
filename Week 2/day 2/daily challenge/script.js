let sentence= 'The movie is not that bad really, I like it';
let sent= sentence.split (" ");
console.log(sent)

let wordNot = sent.indexOf("not");
let wordBad = sent.indexOf("bad");

let count= wordNot-wordBad+1

if (wordNot<wordBad){
   sent.splice(3, 3, "good")
   console.log(sent.join(" "))
}
  
else{
   console.log(sentence)
}


