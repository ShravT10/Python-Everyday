#A number is an Armstrong number if the
#  sum of the cubes of its digits is equal to the number itself.
# (For 3-digit numbers: 153 → 1³ + 5³ + 3³ = 153)

# Write a function is_armstrong(n) that checks this.

def armstrong(s):
    ref = 0
    for i in str(s):
        c = int(i)**len(str(s))
        ref = ref + c

    return ref == s

s = int(input("Enter number : "))
print(armstrong(s))

