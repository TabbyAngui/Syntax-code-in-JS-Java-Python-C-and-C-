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
//Operators: Arithmetic, assignment, comparative and logical
//Arithmetic operators, the value is constant

a = 4;
console.log("Addition example: a+4 = ",a+4);
console.log("Substraction example: a-4 = ",a-4);
console.log("Multipilcation example: a*4 = ",a*4);
console.log("Division example: a/4 = ",a/4);
console.log("Remainder example: a%4 = ",a%4);
console.log("Post increment example: a++ = ",a++);
console.log("Post decrement example: a-- = ",a--);
console.log("Pre increment example: ++a = ",++a);
console.log("Pre decrement example: --a= ",--a);
console.log("Exponential/ power or a number raised: a**4 = ",a**4);

//assignment operator, takes the newest value of a

a = 5;
console.log("Assigning value: a = 5", a);
console.log("Adding assigned value: a += 5", a += 5);// a = a + 5
console.log("Subtracting assigned value: a -= 5", a -= 5);// a = a - 5
console.log("Multiplying assigned value: a *= 5", a*= 5);// a = a * 5
console.log("Dividing assigned value: a /= 5", a /= 5);// a = a / 5
console.log("Remainder assigned value: a %= 5", a %= 5);// a = a % 5
console.log("Exponentiating assigned value: a**= 3", a **= 3);// a = a**3

//comparative operator,gives value as true or false after comparison, They include:

console.log("2 == 2, True or False: ", 2 == 2); // equal to [==]
console.log("2 != 2, True or False: ", 2 != 2); // Not equal to [!=]
console.log("2.00 === 2, True or False: ", 2.0 === 2); // strictly equal to [===]
console.log("2.01 !== 2, True or False: ", 2.01 !== 2); // strictly not equal to [!==]
console.log("7 > 2, True or False: ", 7 > 2); // greater than [>]
console.log("4 < 2, True or False: ", 4 < 2); // equal to [<]
console.log("2.0 >= 2, True or False: ", 2.0 >= 2); // greater or equal to [>=]
console.log("3.2 <= 2, True or False: ", 3.2 <= 2); // less or equal to [<=]

//logic operators AND [&&], NOT[!], OR [||]

a =  7;

console .log(a > 2) && (a < 1);
console .log(a > 5) && (a < 10);
console .log(a > 2) || (a < 1);
console .log(a > 5) || (a < 10);
console.log(!(a > 1));
console.log(!(a > 10));

// bitwise operators, works on bits...changes numbers to bits then do logical operations
//i.e 5 & 3 :5 = 0101 and 3 = 0011 rules of bit 1 & 1 = 1 , 0 & 1 = 0, 1 & 0 = 0, 0 & 0 = 0
//doing the operation 5 & 3 = 0001 which is 1

console.log("5 & 3", 5 & 3); //BITWISE AND
console.log("5 | 3", 5 | 3); //BITWISE OR
console.log("5 ^ 3", 5 ^ 3); //BITWISE XOR
console.log(" ~ 5", ~ 5 );   //BITWISE NOT
console.log("5 << 3", 5 << 3);//Something about shift but i dontget it HA!
console.log("5 >>3", 5 >> 3);
console.log("5 >>>3", 5 >>> 3);

