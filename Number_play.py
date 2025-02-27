import random


target_number = random.randint(1, 100)

attempts = 0
max_attempts = 7

while attempts < max_attempts:
    try:
        
        user_input = input(f"Attempt {attempts + 1}/{max_attempts} - Guess a number between 1 & 100: ")
        user_guess = int(user_input)  
       
        attempts += 1
        
        if user_guess == target_number:
            print("Congratulations! You guessed the right number!")
            break  
        
        
        elif user_guess < target_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
    
    except ValueError:  
        print("This is not a valid number, try again")

if attempts == max_attempts and user_guess != target_number:
    print(f"Sorry! You've used all {max_attempts} attempts. The correct number was {target_number}.")
