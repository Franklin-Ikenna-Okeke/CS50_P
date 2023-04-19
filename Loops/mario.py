def main():
    print_column(3)
    print_row(5)
    print_square(3)

def print_column(height):
    for _ in range(height):
        print("#")
        #print("#\n" * height, end="")

def print_row(width): 
    print("?" * width)  

#Nested Loop

def print_square(size):
    
     #For each row in Square   
    for i in range(size):

        # For each brick in row
        for j in range(size):
            
            #Print brick
            print("#", end="")  
        print()     


main()        
