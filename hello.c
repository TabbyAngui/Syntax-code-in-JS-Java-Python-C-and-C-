#include <stdio.h>
#include <stdbool.h>
int main(){
printf("Hello World\n");
int x;
x= 20;
printf("The lucky number x:%d\n",x);
//declaring every type of variable:. integer, decimal,character and string.

char Grade = 'A';
char name[] = "Jaden";
int Class = 8;
float Avemark = 79.8f;
double Clusterpoint = 4.35;
printf("Did you know %s of class %d got an %c of %f with a cluster point of %f!\n",name,Class,Grade,Avemark,Clusterpoint);
// variable that is unique in C/C++, that is assigned to variables in relation to storage, that somehow becomes a non-issue in python since rpi have huge storage capacity. assigning variable depending on memory, saves on storage. in C we have the short that's a 16bit, and long for 64bit..used for long loops i.e timestamp etc

unsigned short us = 65535;  // 16-bit unsigned
long long lo = 32233720304567;  // 64-bit (LL suffix)
bool flag = true;           // C99+ boolean
printf("unsigned short: %hu \n", us);
printf("long: %lld \n", lo);        
printf("boolean: %d \n", flag);  // 1=true, 0=false
    
    return 0;
}