#Global variable
user_name = input("Enter your name: ")

#Function with no return and no parameters
def greeting_message():
    print("Hello! This is basic Python program that display a user's name.")

#Function with user input as parameter and no return statement
def display_name(user_name):
    print("My name is ", user_name)

#Greet user function call
greeting_message()
#Display function call after greeting user
display_name()
