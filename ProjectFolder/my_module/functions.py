# Imports required to run functions
from os import system, name
from sys import exit
from time import sleep
from random import randint

def game_start():
    """Greet the user starting the game, 
    also prompting a choice to play
    
    Parameters
    ---------------
    N/A
    
    Returns
    ---------------
    N/A
    """
    # Greets user, prompts for name, and asks if they are ready
    input("Hello there, welcome to the number guessing game! " 
          "What is your name? \n \n") 
    print("\nAre you ready to play?") 

    # Uses .upper() so that the input is not case sensitive
    game_choice = input("Enter 'YES' to start the game, "    
                        "or enter 'NO' to quit. \t").upper() 
    game_loop = True # Intialized as true to make game_loop repeat

    while game_loop: # Repeatedly prompts user with different game choices

        console_clear(1) # Clear console with 1 second delay

        # If user enters "YES", the game starts using the game_number function
        # below. If user enters "NO", they are prompted to system exit.  If 
        # "YES" or "NO" are not entered, the greeting starts over
        if game_choice == "YES": 
            console_clear(1)     
            game_number()

        elif game_choice == "NO":  
            console_clear(1)      
            sys.exit()

        else: 
            game_start()


def game_number():
    """Obtain guessed input from user for a total of 3 attempts, 
    check against random generated number, and display output
    
    Parameters
    ---------------
    N/A
    
    Returns
    ---------------
    N/A
    """
    
    total_guesses = 0 # Initializes total number of guesses as 0 when game starts
    rand_number = randint(1,20) # Creates a random number between 1 and 20
    print("\nThe number you shall guess is between 1 and 20." 
          " You have 3 guesses.")

    while total_guesses < 3: # Ensures user only recieves 3 attempts

        print("Enter your guess below.") # Prompts user to enter guess

        # Notifies user which attempt they are on
        if total_guesses == 0:
            print("This is your first attempt. \t") 
        if total_guesses == 1:
            print("This is your second attempt. \t") 
        if total_guesses == 2:
            print("This is your final attempt. \t") 
        
        # Assigns guess to be the input as well as an 
        # integer value for guessing the random number
        guess = input() 
        guess = int(guess)
        
        total_guesses = total_guesses + 1 # Tracks number of total guesses used

        # Helps user confine their guesses based on clues given by the game
        if guess < rand_number:
            print("\nYour guess is below the value of the random number!")
        if guess > rand_number:
            print("\nYour guess is above the value of the random number!")
        if guess == rand_number:
            correct_guess(total_guesses)
        if guess != rand_number and total_guesses == 3:
            incorrect_guess(rand_number)
            

def correct_guess(total_guesses):
    """Awards the user for correctly guessing 
    the number in the amount of guesses taken
    
    Parameters
    ---------------
    total_guesses: int
                Total number of guesses used to 
                correctly guess the random number
    
    Returns
    ---------------
    N/A
    """
    
    print("\nCongratulations! You guessed the random number in " 
          + str(total_guesses) + " guesses!")
    print("You are now returning to the menu...")
    
    # Clears the console after a 3 second delay, then restarts game
    console_clear(3)
    game_start()
    

def incorrect_guess(rand_number):
    """Critiques the user for incorrectly 
    guessing the number in 3 guesses
    
    Parameters
    ---------------
    rand_number: int
                Random number picked by 
                the bot for the game
    
    Returns
    ---------------
    N/A
    """
    
    print("\nSorry! You are out of attempts. The number I was thinking of was "
          + str(rand_number) + ".")
    print("You can try again starting at the menu...")
    
    # Clears the console after a 3 second delay, then restarts game
    console_clear(3) 
    game_start() 
    

def console_clear(wait_time): 
    """Clears console when ran in terminal, with 
    optional time delay. First attempts to clear the 
    console for Windows, then for Linux and Mac 
    operating systems should the first attempt fail.
    
    Paramaters
    ---------------
    wait_time : int
                Amount of time in seconds for 
                delay before console clear
    
    Returns
    ---------------
    N/A
    """

    sleep(wait_time) # Produces a delay based on input passed through console_clear()

    # These commands only work in the terminal
    try:
        system("cls") # Clears console for users on Windows operating system

    except:
        system("clear") # Clears console for users on Mac and Linux operating systems

game_start()