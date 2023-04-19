x = int(input("What's x? "))
y = int(input("What's y? "))

print(x + y)

a = float(input("What's a? "))
b = float(input("What's b? "))

print(a + b)
z = round(a/b) 
z = round(a/b,2) 
z = a/b
print(f"{z:.2f}")

#use what i learned in functions to advance my cal.

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n

main()    
