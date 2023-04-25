x,s=map(int,input().split());
if x>s:
    print('0')
elif x<s:
    req=s-x
    print('required seats',req)
else:
    print('no seats are required')
