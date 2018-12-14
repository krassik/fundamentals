def gcd2(x, y): 
    while(y): 
        x, y = y, x % y 
    return x 

def generalizedGCD(num, arr):
    # WRITE YOUR CODE HERE

    if num == 1:
        return arr[0]
  
    gcd = gcd2(arr[0], arr[1]) 
  
    for i in range(2, num): 
        gcd = gcd2(gcd, arr[i]) 
      
    return(gcd)


if __name__ == "__main__":
    result = generalizedGCD(5, [2,3,4,5,6])
    print(result)