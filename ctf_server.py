#!/usr/bin/env python3
"""
CTF Server Wrapper - Handles multiple concurrent connections
Run this to start the CTF challenge server on port 9999
"""

import socket
import subprocess
import threading

HOST = '0.0.0.0'
PORT = 9999
SCRIPT_PATH = '/workspace/higher_lower_ctf.py'

def handle_client(conn, addr):
    """Handle a single client connection"""
    print(f"[+] Connected: {addr}")
    
    try:
        # Start the game script as a subprocess
        process = subprocess.Popen(
            ['python3', SCRIPT_PATH],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            bufsize=0
        )
        
        # Send initial banner
        conn.sendall(process.stdout.read(512))
        
        while True:
            # Receive data from client
            data = conn.recv(1024)
            if not data:
                break
            
            # Send to game process
            process.stdin.write(data)
            process.stdin.flush()
            
            # Get response from game process
            response = process.stdout.read(1024)
            if response:
                conn.sendall(response)
                
            # Check if game ended (flag shown or game over)
            if b"flag" in response.lower() or b"Game Over" in response:
                break
                
    except Exception as e:
        print(f"[-] Error with {addr}: {e}")
    finally:
        try:
            process.terminate()
            conn.close()
        except:
            pass
        print(f"[-] Disconnected: {addr}")

def start_server():
    """Start the TCP server"""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)
        print(f"[*] CTF Challenge Server running on {HOST}:{PORT}")
        print(f"[*] Waiting for connections...")
        print(f"[*] Connect with: nc <server_ip> {PORT}")
        
        while True:
            conn, addr = server_socket.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.daemon = True
            thread.start()
            
    except KeyboardInterrupt:
        print("\n[*] Server shutting down...")
    except Exception as e:
        print(f"[!] Server error: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()
