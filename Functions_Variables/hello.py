# Ask user for their name

name = input("What's your name? ")

# To remove whitespace from str
name = name.strip()

# Capitalize user's name

name = name.capitalize() #this capitalize the first character/letter

name = name.title() # Words start with uppercased characters and all remaining cased characters have lower case.


#Say hello to user in a formatted way
print(f"hello, {name}")


## Create a more elegant code for what i have written above in a chained 
name = input("What's your name? ").strip().title()
print(f"hello, {name}") 