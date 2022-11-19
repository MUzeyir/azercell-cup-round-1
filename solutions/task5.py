def test(n):
        if n > 1 and n != 2:
            for i in range(2, int(n/2)+1):
                if (n % i) == 0:
                    return next(d for d in range(n - 1, 0, -1) if n % d == 0)
                    break
                else:
                    return 1
        elif n == 2 :
            return 1
        else :
            return "-"

     
 
n = input()

print(test(int(n)))
