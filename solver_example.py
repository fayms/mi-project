#!/usr/bin/env python3
"""
Example solver script for the Higher/Lower CTF challenge
Demonstrates binary search automation to solve the challenge
"""

import socket

def solve_challenge(host='localhost', port=9999):
    """
    Automate solving the Higher/Lower challenge using binary search
    """
    print(f"[*] Connecting to {host}:{port}...")
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(10)
        s.connect((host, port))
        
        # Receive initial banner
        banner = s.recv(2048).decode()
        print(banner)
        
        # Binary search parameters
        low, high = 1, 100
        max_attempts = 7
        
        for attempt in range(max_attempts):
            # Calculate midpoint for binary search
            guess = (low + high) // 2
            
            print(f"[*] Attempt {attempt + 1}/{max_attempts}: Guessing {guess}")
            
            # Send guess
            s.send(f"{guess}\n".encode())
            
            # Receive response
            response = s.recv(1024).decode()
            print(response)
            
            # Check for win condition
            if "Correct" in response or "flag" in response.lower():
                print("[+] Challenge solved!")
                if "CTF{" in response:
                    print("[*] Flag captured!")
                break
            
            # Check for loss condition
            if "Game Over" in response:
                print("[-] Game over, try again!")
                break
            
            # Adjust search range based on hint
            if "Higher" in response:
                low = guess + 1
            elif "Lower" in response:
                high = guess - 1
        
        s.close()
        
    except ConnectionRefusedError:
        print(f"[!] Error: Could not connect to {host}:{port}")
        print("[*] Make sure the server is running!")
    except socket.timeout:
        print("[!] Error: Connection timed out")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    import sys
    
    # Allow custom host/port from command line
    host = sys.argv[1] if len(sys.argv) > 1 else 'localhost'
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 9999
    
    solve_challenge(host, port)
