sum=0
p=0
bin=int(input('enter any binary number'));
while bin>0:
    r=bin%10
    sum=sum+r*2**p
    bin=bin//10
    p=p+1
print("the target decimal number=",sum)
