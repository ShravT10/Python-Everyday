def checkPrime(n):
    if n == 1:
        print("1 is neither prime nor composite")
    else:
        num = 0
        for i in range(1,n):
            if n%i==0:
                num = num+1
        if num>1:
            print("Not a Prime Number")
        else:
            print("is a prime number")   

n = int(input("Enter your number : "))
checkPrime(n) 
