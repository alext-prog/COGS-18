from functions import *

def test_correct_guess():
    """Tests for the correct_guess function"""
    
    assert callable(correct_guess)
    assert isinstance(correct_guess(2), str)
    assert correct_guess(2) == ("\nCongratulations! You guessed the random number in " + str(2) + 
                                " guesses!" + "\nYou are now returning to the menu...")
        
def test_incorrect_guess():
    """Tests for the incorrect_guess function"""
    
    assert callable(incorrect_guess)
    assert isinstance(incorrect_guess(8), str)
    assert incorrect_guess(8) == ("\nSorry! You are out of attempts. The number I was thinking of was " 
                                + str(8) + ". \nYou can try again starting at the menu...")