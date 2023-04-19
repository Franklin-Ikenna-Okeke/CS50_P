# Define a function called coke_machine
def coke_machine():

    #Initialize the amount due and amount inserted variables
    amount_due = 50
    amount_inserted = 0

    # Loop until the amount inserted is greater than or equal to the amount due
    while amount_inserted < amount_due:

        # Use a for loop to limit the number of times the user can input coins
        for i in range(5):

            # Prompt the user to insert a coin and convert the input to an integer
            coin = int(input("Insert Coin: "))

            # Check if the coin is a valid denomination
            if coin in [25, 10, 5]:

                # Add the coin to the amount inserted and display the amount due
                amount_inserted += coin
                print("Amount Due:", amount_due - amount_inserted)

                # Break out of the for loop once a valid coin is inserted
                break
            else:

                # Display the amount due again if an invalid coin is inserted
                print("Amount Due:", amount_due - amount_inserted)

                # Break out of the for loop to allow the user to input another coin
                break



    # Calculate the change owed to the user and display it
    change = amount_inserted - amount_due
    print("Change Owed:", change)

# Call the coke_machine function to start the program
coke_machine()