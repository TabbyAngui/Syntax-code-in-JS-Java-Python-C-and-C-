public class hello{

public static void main(String[] args){

System.out.println("Hello World");

int age = 24;
System.out.println("Tabby is " + age +" years old.");

//declaring every type of variable:. integer, decimal,character and string.


char grade = 'A';
String name = "Jaden";
int Class = 8;
float Avemarks = 79.8f;
double Clusterpoint = 4.35;
System.out.println("Did you know " + name + "of class " + Class + " got an " + grade + " of " + Avemarks + " which is a cluster point of : " + Clusterpoint);
//there are other variable types that are important to note, 
//variables are assigned a certain memory size depending on the type of var i.e char 8bit, int 32bit, 
//can either be  byte -128 to 127 which is an 8bit data length
//short which is a 16bit data length
//long which is a 64bit

byte b = 127;           // 8-bit: -128 to 127
short s = 32767;        // 16-bit: -32,768 to 32,767
long l = 9223372036854775807L;  // 64-bit (needs L suffix)


boolean flag = true;    // true/false only
        
System.out.println("byte: " + b);
System.out.println("short: " + s);
System.out.println("long: " + l);
System.out.println("boolean: " + flag);


// Operands, we have arithmetic, assigning, comparative, logic, bitwise among others as discussed below
//Arithmetic Operands
System.out.println();
int x = 24, y = 3;
System.out.println("Addition: "+ (x + y));
System.out.println("Substraction: "+ (x - y));
System.out.println("Multiplication: "+ (x * y));
System.out.println("Division: "+ (x / y));
System.out.println("Remainder: "+ (x % y));

//Assigning operator
int num;
//assigning a value
System.out.println();
num = 5;
System.out.println("Assigning a value:"+num);
num += 7;
System.out.println("Add such that a = a + 7: " +num);
num -= 4;
System.out.println("Substract such that a = a -4: " +num);
num /= 2;
System.out.println("Divide such that a = a/2: " +num);
num *= 4;
System.out.println("Multiply such that a = a * 4: "+num);

//Relational or comparative operators

int g = 4, h = 3;
System.out.println();
System.out.println("a is " + g + " and b is " +h);
System.out.println("a == b : " + (g == h));
System.out.println("a != b : " + (g != h));
System.out.println("a > b : " + (g > h));
System.out.println("a < b : " + (g < h));
System.out.println("a >= b : " + (g >= h));
System.out.println("a <= b : " + (g <= h));

//logic operators AND, OR, NOT

System.out.println();
System.out.println((g != h) && (g > h));
System.out.println((g != h) && (g < h));
System.out.println((g != h) || (g > h));
System.out.println((g != h) || (g < h));
System.out.println(!(g == h));
System.out.println(!(g > h));

//Unary operator involves increment, decrement operators.
int Result = 14 + 11;
int Result1 = ++ Result;
int Result2 = -- Result;
System.out.println();
System.out.println("Unary operators involve incremental operator (++x) and decremental operator (--x) ");
System.out.println(Result1);
System.out.println(Result2);

//Other type of operators include

System.out.println();
System.out.println("The operator 'instance of' checks whether a variable is in a class defined");
 String str = "Programiz";
 boolean result;

    // checks if str is an instance of
    // the String class

  result = str instanceof String;
  System.out.println("Is str an object of String? " + result);

//Java ternary operator/conditional operator is like the short form of if-else then,
//variable = Expression ? expression 1: espression 2


int februarydays = 29;
String month;

month = (februarydays == 28) ? " leap year" : " ordinary year" ;
System.out.println(month);





}
}
