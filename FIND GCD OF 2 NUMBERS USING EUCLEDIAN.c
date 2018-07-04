#include<stdio.h>

void main()
{
int a,b,q,r,r1,r2,gcd;
printf("Enter First Number :");
scanf("%d",&a);
printf("Enter Second Number :");
scanf("%d",&b);
r1=a;
r2=b;
while(r2!=0)
{
r=r1%r2;
q=r1/r2;
r1=r2;
r2=r;
}
gcd=r1;
printf("The gcd of %d and %d is : %d",a,b,gcd);
}

