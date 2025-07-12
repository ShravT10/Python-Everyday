# Write a function fibonacci(n) 
# that returns the first n terms of the Fibonacci sequence.

# Input: 5
# Output: [0, 1, 1, 2, 3]

def fibaconni(n):
    s0 = 0
    s1 = 1 
    s2 = s0 + s1
    a = [s0,s1,s2]
    for i in range(0,n-3):
        s0 = s1
        s1 = s2 
        s2 = s0 + s1
        a.append(s2)
    return a

print(fibaconni(6))

#gpt

def fibacnni(n):
    if n<=0:
        return []
    elif n==1:
        return [0]
    
    fib = [0,1]
    while len(fib)<n:
        fib.append(fib[-1] + fib[-2])
    return fib

print(fibacnni(5))
print(fibacnni(5)) 
