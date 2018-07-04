#include <stdio.h>
int primeno(int n, int i)
{
    if (i == 1)
    {
        return 1;
    }
    else
    {
       if (n % i == 0)
       {
         return 0;
       }
       else
       {
         return primeno(n, i - 1);
       }       
    }
}

int gcd(int b,int n)
{
	int q,r,r1,r2,t,t1,t2;
	r1=n;
	r2=b;
	t1=0;
	t2=1;
	while(r2!=0)
	{
		q=r1/r2;
		r=r1-(q*r2);
		r1=r2;
		r2=r;
		t=t1-(q*t2);
		t1=t2;
		t2=t;
	}
	if(r1==1)
		return t1;
	else
		return 0;
}

void main()
{
	int n,p,count=0,g;
	
	while(count==0)
	{
		printf("Enter p for Zp ");
		scanf("%d",&n);
		if(n<0)
			printf("p is not a prime number & greater than 0. Enter again ");
		else
			count=primeno(n,n/2);
	}
	count=0;
	while(count==0)
	{
		printf("Enter b  ");
		scanf("%d",&p);
		if(p>=n || p<0)
		{
			printf("b should be less than p & greater than 0. Enter again ");
		}
		else
			count=1;
		
	}
	
	g=gcd(p,n);
	if(g<0)
		g=g+n;
	if(gcd==0)
		printf("The multiplicative inverse does not exist");
	else
		printf("The multiplicative inverse of %d in Z%d is %d \n\n",p,n,g);
}

