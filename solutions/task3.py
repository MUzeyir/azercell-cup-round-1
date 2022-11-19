# of squares inside an n*n grid
def cntSquares(n) :
 
    squares = 0;
    for i in range(1, n + 1) :
        squares += i ** 2;
 
    return squares;
 
# Driver code
if __name__ == "__main__" :
 
    num = input()
 
    print(cntSquares(int(num)));


