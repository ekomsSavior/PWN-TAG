#!/bin/bash
echo "[*] Starting PWN TAG server on port 8080..."
cd "$(dirname "$0")"
python3 -m http.server 8080 &
echo "[*] Starting ngrok..."
ngrok http 8080
