var stringS = "Hello World!";
var stringR = "lo W ";

var a = "Blackwood";
var b = "Clementon";


function concat(string1, string2, index){
    let newString = "";
    for(let i = 0; i < string1.length; i++){
        if(i <= index){
            newString = newString.concat(string1[i]);
            continue;
        }
        if (i == index + 1){
            newString = newString.concat(string2);
        }
        else {
            newString = newString.concat(string1[i]);
        }
    }
    console.log("Your result is: " + newString);
}

concat(a, b, 7);