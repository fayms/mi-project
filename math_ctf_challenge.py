#!/usr/bin/env python3
"""
Reverse Engineering CTF Challenge - Math Puzzle
Students must solve progressively harder math problems to get the flag.
Difficulty increases in polynomial time (O(n^2)).
"""

import hashlib
import time
from typing import Tuple

# Hidden flag (students need to reverse engineer or complete the challenge)
FLAG = "CTF{r3v3rs3_3ng1n33r1ng_m4th_m4st3r_2024}"

def verify_answer(problem_type: str, expected: int, user_answer: int) -> bool:
    """Verify if the user's answer is correct."""
    return expected == user_answer

def generate_problem(level: int) -> Tuple[str, int, str]:
    """
    Generate math problems with increasing difficulty.
    Difficulty grows in polynomial time O(n^2).
    """
    if level == 1:
        # Level 1: Simple addition
        problem = "What is 5 + 7?"
        answer = 12
        hint = "Basic arithmetic"
    elif level == 2:
        # Level 2: Multiplication
        problem = "What is 13 * 4?"
        answer = 52
        hint = "Multiplication table"
    elif level == 3:
        # Level 3: Square root
        problem = "What is the square root of 144?"
        answer = 12
        hint = "Perfect square"
    elif level == 4:
        # Level 4: Quadratic expression
        problem = "If x = 5, what is x^2 + 3x - 10?"
        answer = 30  # 25 + 15 - 10
        hint = "Substitute and calculate"
    elif level == 5:
        # Level 5: Sum of series
        problem = "What is the sum of first 20 natural numbers? (1+2+3+...+20)"
        answer = 210  # n*(n+1)/2 = 20*21/2
        hint = "Formula: n*(n+1)/2"
    elif level == 6:
        # Level 6: Prime factorization
        problem = "What is the largest prime factor of 13195?"
        answer = 29  # 13195 = 5 * 7 * 13 * 29
        hint = "Factorize completely"
    elif level == 7:
        # Level 7: Fibonacci sequence
        problem = "What is the 15th Fibonacci number? (F(1)=1, F(2)=1)"
        answer = 610
        hint = "Each number is sum of previous two"
    elif level == 8:
        # Level 8: Modular arithmetic
        problem = "What is (7^25) mod 11?"
        answer = 10  # Using Fermat's little theorem
        hint = "Use modular exponentiation"
    elif level == 9:
        # Level 9: Combinatorics
        problem = "How many ways to choose 3 items from 10? (C(10,3))"
        answer = 120  # 10!/(3!*7!) = 120
        hint = "Combination formula"
    elif level == 10:
        # Level 10: Complex polynomial
        problem = "Evaluate: 2^10 + 3^6 - 5^4"
        answer = 4096 + 729 - 625  # = 4200
        answer = 4200
        hint = "Calculate each term separately"
    else:
        # Final level: Hash verification
        problem = f"What is the SHA256 hash of '{FLAG}'? (First 8 hex chars)"
        hash_value = hashlib.sha256(FLAG.encode()).hexdigest()[:8]
        answer = hash_value
        hint = "You should know the flag by now!"
    
    return problem, answer, hint

def calculate_fibonacci(n: int) -> int:
    """Helper function for Fibonacci calculation."""
    if n <= 2:
        return 1
    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

def main():
    print("=" * 60)
    print("REVERSE ENGINEERING CTF CHALLENGE")
    print("=" * 60)
    print("\nWelcome, hacker!")
    print("Solve all math problems to reveal the flag.")
    print("Difficulty increases with each level.\n")
    print("Type 'hint' for a hint, 'quit' to give up.\n")
    
    total_levels = 10
    current_level = 1
    
    start_time = time.time()
    
    while current_level <= total_levels:
        print(f"\n{'='*60}")
        print(f"LEVEL {current_level}/{total_levels}")
        print(f"{'='*60}")
        
        problem, answer, hint = generate_problem(current_level)
        print(f"\nProblem: {problem}")
        
        attempts = 0
        max_attempts = 3
        
        while attempts < max_attempts:
            user_input = input(f"\nYour answer (attempt {attempts + 1}/{max_attempts}): ").strip()
            
            if user_input.lower() == 'quit':
                print("\nGiving up so soon? The flag remains hidden...")
                print(f"You reached level {current_level}")
                return
            
            if user_input.lower() == 'hint':
                print(f"Hint: {hint}")
                continue
            
            try:
                # Try to parse as integer first
                user_answer = int(user_input)
            except ValueError:
                # For level 10, accept string answer (hash)
                user_answer = user_input
            
            if verify_answer(problem, answer, user_answer):
                print("\n✓ Correct! Well done!")
                break
            else:
                print("✗ Incorrect. Try again!")
                attempts += 1
        
        if attempts >= max_attempts:
            print(f"\nToo many failed attempts! The correct answer was: {answer}")
            print("Game Over!")
            return
        
        current_level += 1
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    print("\n" + "=" * 60)
    print("CONGRATULATIONS!")
    print("=" * 60)
    print("\nYou've solved all the problems!")
    print(f"Time taken: {elapsed_time:.2f} seconds")
    print("\n" + "*"*60)
    print(f"HERE IS YOUR FLAG: {FLAG}")
    print("*"*60)
    print("\nWell done, reverse engineering master!")

if __name__ == "__main__":
    main()
