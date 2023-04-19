def hello(to):
    print("hello,", to)

name = input("What's your name? ")
hello(name)    

# I can give my parameter a default value incase the function is called without an argument 

def hello1(to="World"):
    print("hello,",to)


def main():
    name = input("What's your name? ")
    hello(name)  

def hello1(to="World"):
    print("hello,",to)

main()            
