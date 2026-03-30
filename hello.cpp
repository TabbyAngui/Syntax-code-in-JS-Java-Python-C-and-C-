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
return 0;
}