a,b,c = input().split()
sum = int(a) + int(b) + int(c)

largest = 0

if(int(sum) != 180) :
    print(-1)
elif(int(a) == 0 or int(b) == 0 or int(c) == 0) :
    print(-1)
else :
    if a > b and a > c:
        largest = a
    elif b > a and b > c:
        largest = b
    elif c > a and c > b:
        largest = c
    print(largest)
