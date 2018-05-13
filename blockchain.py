# Initializing our blockchain list
blockchain: list = []

def get_last_bloackchain_value():
    """ Returns the last value of the current blockchain list """
    return blockchain[-1]

def add_value(transaction_amount, last_transaction=[1]): #default value
    blockchain.append([last_transaction, transaction_amount])

def get_user_input():
    return float(input("Please enter the transaction amount: "))


# To get the values from the user on run time
input_amount = get_user_input()
add_value(input_amount)

input_amount = get_user_input()
add_value(last_transaction=get_last_bloackchain_value(),
          transaction_amount=input_amount)  # keyword arguments

input_amount = get_user_input()
add_value(input_amount, get_last_bloackchain_value())

print(blockchain)
