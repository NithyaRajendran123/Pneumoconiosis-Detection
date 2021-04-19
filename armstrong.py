n=int(input("enter a number"))
sum=0
num=n
while(num>0):
    r=num%10
    a=r*r*r
    sum=sum+a
    num=num//10
if(n==sum):
    print("armstrong",n)
else:
    print("not armstrong",n)
 