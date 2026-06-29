#!/usr/bin/env python3
"""
RE CTF Challenge: Polynomial Math Gauntlet
Students must solve 10 math problems of increasing polynomial complexity.
The flag is obfuscated and only revealed after answering all 10 questions correctly.
"""

import time
import sys
import random

# Obfuscated flag (XOR encoded with key 0x5A)
FLAG_ENCODED = [25, 14, 28, 33, 40, 105, 44, 105, 40, 41, 105, 5, 105, 52, 61, 107, 52, 105, 105, 40, 107, 52, 61, 5, 55, 110, 46, 50, 5, 55, 110, 41, 46, 105, 40, 5, 104, 106, 104, 110, 39]

def decode_flag():
    """Decode the obfuscated flag"""
    key = 0x5A
    return "".join(chr(byte ^ key) for byte in FLAG_ENCODED)

def generate_problem(level):
    """Generate math problems with polynomial time complexity growth"""
    if level == 1:
        a = random.randint(10, 50)
        b = random.randint(10, 50)
        return f"What is {a} + {b}?", a + b
    
    elif level == 2:
        a = random.randint(5, 20)
        b = random.randint(5, 20)
        return f"What is {a} × {b}?", a * b
    
    elif level == 3:
        n = random.randint(5, 15)
        return f"What is the sum of squares from 1 to {n}?", sum(i*i for i in range(1, n+1))
    
    elif level == 4:
        n = random.randint(10, 20)
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return f"What is the {n}th Fibonacci number?", a
    
    elif level == 5:
        n = random.randint(3, 10)
        return f"What is the sum of cubes from 1 to {n}?", sum(i**3 for i in range(1, n+1))
    
    elif level == 6:
        n = random.randint(100, 500)
        def count_prime_factors(num):
            count = 0
            d = 2
            while d * d <= num:
                while num % d == 0:
                    count += 1
                    num //= d
                d += 1
            if num > 1:
                count += 1
            return count
        return f"How many prime factors does {n} have (with multiplicity)?", count_prime_factors(n)
    
    elif level == 7:
        base = random.randint(2, 10)
        exp = random.randint(5, 15)
        mod = random.randint(50, 200)
        return f"What is {base}^{exp} mod {mod}?", pow(base, exp, mod)
    
    elif level == 8:
        a = random.randint(100, 500)
        b = random.randint(100, 500)
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        return f"What is GCD({a}, {b})?", gcd(a, b)
    
    elif level == 9:
        a = random.randint(1, 5)
        r = random.randint(2, 4)
        n = random.randint(5, 10)
        total = a * (r**n - 1) // (r - 1)
        return f"What is the sum of geometric series: {a} + {a*r} + ... ({n} terms, ratio {r})?", total
    
    elif level == 10:
        n = random.randint(10, 20)
        k = random.randint(3, min(7, n-3))
        def comb(n, k):
            if k > n or k < 0:
                return 0
            result = 1
            for i in range(k):
                result = result * (n - i) // (i + 1)
            return result
        return f"What is C({n},{k}) (combinations)?", comb(n, k)
    
    return "Invalid level", 0

def main():
    print("=" * 60)
    print("REVERSE ENGINEERING CTF CHALLENGE")
    print("Polynomial Math Gauntlet - 10 Levels")
    print("=" * 60)
    print("\nRules:")
    print("- Solve 10 math problems of increasing difficulty")
    print("- Complexity grows polynomially with each level")
    print("- You have 3 attempts per level")
    print("- Type 'hint' for a hint (costs 1 attempt)")
    print("- Type 'quit' to exit")
    print("- Answer ALL 10 questions correctly to receive the flag\n")
    
    input("Press Enter to start...")
    start_time = time.time()
    
    level = 1
    
    while level <= 10:
        print(f"\n{'='*40}")
        print(f"LEVEL {level}/10")
        print(f"{'='*40}")
        
        question, correct_answer = generate_problem(level)
        attempts = 3
        
        while attempts > 0:
            print(f"\nQuestion: {question}")
            print(f"Attempts remaining: {attempts}")
            
            user_input = input("Your answer: ").strip()
            
            if user_input.lower() == 'quit':
                print("\nChallenge aborted. Flag locked forever.")
                sys.exit(0)
            
            if user_input.lower() == 'hint':
                attempts -= 1
                if level <= 3:
                    print(f"Hint: Basic arithmetic (complexity ~O(n^{level}))")
                elif level <= 6:
                    print(f"Hint: Iterative approach (complexity ~O(n^{level}))")
                else:
                    print(f"Hint: Advanced algorithm (complexity ~O(n^{level}))")
                continue
            
            try:
                user_answer = int(user_input)
                
                if user_answer == correct_answer:
                    print("✓ Correct!")
                    level += 1
                    break
                else:
                    print("✗ Wrong answer!")
                    attempts -= 1
                    
                    if attempts == 0:
                        print("\nGame Over! You failed this level.")
                        print("Flag remains locked. Try again from the start.")
                        sys.exit(0)
                        
            except ValueError:
                print("Please enter a valid number, 'hint', or 'quit'")
    
    end_time = time.time()
    total_time = end_time - start_time
    
    print("\n" + "=" * 60)
    print("CONGRATULATIONS! ALL 10 LEVELS COMPLETED!")
    print(f"Total time: {total_time:.2f} seconds")
    print("=" * 60)
    
    # Only reveal flag after all 10 questions answered correctly
    flag = decode_flag()
    print(f"\n🏁 FLAG: {flag}")
    print("\nWell done, Reverse Engineer!")
    print("You've conquered the Polynomial Math Gauntlet!")

if __name__ == "__main__":
    main()
