#!/usr/bin/env python3
"""
RE CTF Challenge: Higher or Lower Game
Students must reverse engineer this binary to understand the logic
and automate the guessing process to get the flag.
"""

import random
import sys
import os

# Flag is obfuscated - students need to reverse engineer this
FLAG = "CTF{r3v3rs3_3ng1n33r1ng_m4st3r_2024}"

def obfuscate_flag():
    """Simple obfuscation to make reversing more challenging"""
    encoded = []
    for i, char in enumerate(FLAG):
        encoded.append(ord(char) ^ (i % 7))
    return encoded

def deobfuscate_flag(encoded):
    """Deobfuscate the flag"""
    decoded = ""
    for i, val in enumerate(encoded):
        decoded += chr(val ^ (i % 7))
    return decoded

# Store obfuscated flag
OBFUSCATED_FLAG = obfuscate_flag()

def get_number_to_guess():
    """Generate a random number between 1 and 100"""
    return random.randint(1, 100)

def play_game():
    """Main game loop"""
    print("=" * 50)
    print("Welcome to the Higher/Lower Challenge!")
    print("=" * 50)
    print("I'm thinking of a number between 1 and 100.")
    print("You have 7 attempts to guess it.")
    print("Good luck!\n")
    
    target_number = get_number_to_guess()
    attempts = 0
    max_attempts = 7
    
    while attempts < max_attempts:
        try:
            guess = input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: ")
            
            # Validate input
            if not guess.isdigit():
                print("Please enter a valid number between 1 and 100.\n")
                continue
                
            guess = int(guess)
            
            if guess < 1 or guess > 100:
                print("Number must be between 1 and 100.\n")
                continue
            
            attempts += 1
            
            if guess == target_number:
                print(f"\n🎉 Correct! The number was {target_number}!")
                print("Congratulations! You've completed the challenge!")
                print("\nHere's your flag:")
                print(deobfuscate_flag(OBFUSCATED_FLAG))
                return True
            elif guess < target_number:
                print("📈 Higher!\n")
            else:
                print("📉 Lower!\n")
                
        except EOFError:
            print("\nConnection closed.")
            return False
        except Exception as e:
            print(f"Error: {e}\n")
            continue
    
    print(f"\n😞 Game Over! The number was {target_number}.")
    print("Better luck next time!")
    return False

def main():
    """Main entry point"""
    try:
        success = play_game()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\nGame interrupted.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
