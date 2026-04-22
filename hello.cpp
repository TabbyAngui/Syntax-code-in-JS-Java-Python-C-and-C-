#include <iostream>
#include <string>
using namespace std;
int main () {
cout<<"Hello World"<<endl;

int a;
a = 24;
std::cout<<"I am "<<a<<" years old"<<endl;
printf("I am %d years old\n", a);

//declaring every type of variable:. integer, decimal,character and string.

char grade = 'A';
string name = "Jaden";
int Class = 8;
float Avemarks = 79.8f;
double Clusterpoint = 4.35;
std::cout<<"Did you know "<<name<<" of class "<<Class<<" got an "<<grade<<" of "<<Avemarks<<" which is a cluster point of : "<<Clusterpoint<<std::endl;
// variable that is unique in C/C++, that is assigned to variables in relation to storage, that somehow becomes a non-issue in python since rpi have huge storage capacity. assigning variable depending on memory, saves on storage. in C++ we have the short that's a 32bit, and long for 64bit..used for long loops i.e timestamp etc

short z;
long b;
long long c;
long double d;

printf("size of short = %d bytes\n", sizeof(z));
printf("size of long = %d bytes\n", sizeof(b));
printf("size of long long = %d bytes\n", sizeof(c));
printf("size of long double= %d bytes\n", sizeof(d));

//signed - allows for storage of both positive and negative numbers
//unsigned - allows for storage of only positive numbers

unsigned int ui = 4294967295U;  // 32-bit unsigned (U suffix)
long long ll = 9223372036854775807LL;  // 64-bit
    
cout << "unsigned int: " << ui << endl;
cout << "long long: " << ll << endl;

//assigning a boolean you use bool usually the flag false is 0 and true is 1, when you use boolalpha it prints true/false, when you use bool only it prints 1/0
bool flag = false;
cout << "bool: " << boolalpha << flag << endl;  // "true"/"false"

// WITHOUT boolalpha (default)
cout << flag << endl;     // Prints: 0

// WITH boolalpha  
cout << boolalpha << flag << endl;  // Prints: false
return 0;
}