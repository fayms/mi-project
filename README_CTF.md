# RE CTF Challenge: Higher/Lower Game

## Challenge Description
Students must reverse engineer this Python binary to understand the game logic and automate the guessing process. The goal is to correctly guess a randomly generated number between 1 and 100 within 7 attempts.

## Learning Objectives
- Reverse engineering Python bytecode
- Understanding obfuscation techniques
- Automating interactions with network services
- Binary analysis using tools like `pycdc`, `uncompyle6`, or Ghidra

## Setup Instructions

### Option 1: Run locally for testing
```bash
python3 higher_lower_ctf.py
```

### Option 2: Set up netcat server (Recommended for CTF)

**Method A: Using netcat with a loop**
```bash
# Start the server on port 9999
while true; do nc -lvp 9999 -e /workspace/higher_lower_ctf.py; done
```

**Method B: Using socat (more robust)**
```bash
# Install socat if not already installed
sudo apt-get install socat

# Start the server on port 9999
socat TCP-LISTEN:9999,reuseaddr,fork EXEC:/workspace/higher_lower_ctf.py
```

**Method C: Using Python socket server**
```bash
python3 ctf_server.py
```

## Connecting to the Challenge
```bash
nc <server_ip> 9999
```

## Challenge Details

### Game Rules
1. The program generates a random number between 1 and 100
2. Players have 7 attempts to guess the number
3. After each guess, the program hints "Higher" or "Lower"
4. Successfully guessing the number reveals the flag

### Obfuscation
The flag is XOR-obfuscated with a rotating key (0-6). Students must:
1. Decompile or analyze the Python bytecode
2. Identify the obfuscation pattern
3. Either solve the game legitimately or extract the flag directly

### Expected Solution Path
1. **Reconnaissance**: Use `file`, `strings`, or examine the source if available
2. **Decompilation**: Use `pycdc` or `uncompyle6` if compiled to `.pyc`
3. **Analysis**: Identify the random number generation and flag obfuscation
4. **Exploitation**: 
   - Write a script to automate binary search guessing
   - OR extract and deobfuscate the flag directly from the code

### Example Exploit Script (Binary Search)
```python
import socket

def solve():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('challenge.ctf.local', 9999))
    
    low, high = 1, 100
    
    for attempt in range(7):
        mid = (low + high) // 2
        s.send(f"{mid}\n".encode())
        response = s.recv(1024).decode()
        
        if "Correct" in response:
            print(response)
            break
        elif "Higher" in response:
            low = mid + 1
        elif "Lower" in response:
            high = mid - 1
    
    s.close()

solve()
```

## Flag Format
`CTF{r3v3rs3_3ng1n33r1ng_m4st3r_2024}`

## Difficulty Rating
⭐⭐☆☆☆ (Beginner-Intermediate)

## Tags
- reverse-engineering
- python
- automation
- obfuscation
- netcat

## Notes for CTF Organizers
1. Consider compiling the Python script to `.pyc` bytecode for added difficulty
2. You can modify the flag in the source code before deployment
3. Adjust the number range or attempts to change difficulty
4. Monitor connections and log flags captured for scoring
