#!/usr/bin/env python3

import subprocess
import time
import os
import requests
import re

def start_http_server():
    print("[*] Launching local Python HTTP server on port 8080...")
    subprocess.Popen(["python3", "-m", "http.server", "8080"], cwd=os.getcwd())

def start_ngrok():
    print("[*] Starting ngrok tunnel...")
    subprocess.Popen(["ngrok", "http", "8080"], cwd=os.getcwd())
    time.sleep(3)  # allow ngrok to initialize
    try:
        tunnels = requests.get("http://127.0.0.1:4040/api/tunnels").json()
        for tunnel in tunnels["tunnels"]:
            if tunnel["proto"] == "https":
                print(f"[+] 🔗 NGROK URL: {tunnel['public_url']}")
                return tunnel['public_url']
    except Exception as e:
        print(f"[!] Failed to get ngrok URL: {e}")
        return None

if __name__ == "__main__":
    start_http_server()
    url = start_ngrok()
    if url:
        print(f"[→] Write this to your NFC tag: {url}/payloads/test_shell.html")
