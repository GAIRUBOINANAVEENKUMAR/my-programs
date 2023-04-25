#sum of factors of a given number
n=int(input("enter any number"))
for i in range(1,n+1):
    if n%i==0:
        sum=0
        sum+=i
        print("sum of factors",sum)
print('done')
