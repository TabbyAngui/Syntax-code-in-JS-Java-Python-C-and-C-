console.log("Hello world!");
let age = 24;
console.log("Hii I am " + age + " years old");
//declaring every type of variable:. integer, decimal,character and string.

let name = "Jaden";
let Grade = 'A';
let Class = 8;
let Avegrade = 79.8;
let Clusterpoint = 4.35;

console.log("Did you know " + name + "of class " + Class + " got an " + Grade + " of " + Avegrade + " which is a cluster point of : " + Clusterpoint);

// declaring an undefined data
let a;
//or
let a_1 = undefined;
console.log(a,a_1);
//declaring null
let d = null;
console.log(d);
//declaring boolean
let Tabby_bright = true;
console.log(Tabby_bright);

//declaring lists in Js
let vowels = ['a','e','i','o','u'];
console.log(vowels);
let alphabets = {"A" : "Apple", "B" :"Boy", "C":"Cat"};
console.log(alphabets);
let Numbers = [1,2,3,3.4,4.54];
console.log(Numbers);
//Quick summary: [] = arrays/lists, {} = objects/dicts, () = math/grouping.

let Jaden_dets = {
"Name" : "Jaden ",
"Class" : "8 ",
"Grade" : "A ",
"Avemarks" : "79.8 ",
"Clusterpoints" : "4.35 "
};
// the above is an example of key - oblect array or dictionary, where a value {key} is stored data in it. 
//In Py you read the value by naming value but in JS you read the value by naming the array that has the key i.e. Jaden_dets[key]
//`$ is used as alternative of +. It shows where to put  the value 
// for + it would have been console.log(key + ":" +Jaden_dets[key])
console.log("Below are Jaden details:");
for (let key in Jaden_dets) {
    console.log(`${key}: ${Jaden_dets[key]}`);
}




