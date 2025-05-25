# PWN-TAG
"tag to pwn" NFC tag exploit



##Start HTTP Server in Terminal 1

In your ~/PWN_TAG folder:

'''bash
python3 -m http.server 8080
'''
Leave it running — this hosts your payloads.

##2️Start ngrok in Terminal 2

Open a new terminal tab or split window, then run:

'''bash
ngrok http 8080
'''
Copy that https://... link — that’s your live web URL.

## Update test_shell.html in Terminal 3

If you haven’t updated yet:

'''bash
nano payloads/test_shell.html
'''
Replace with your real ngrok link

##Start Listener in Terminal 4

'''bash
python3 listener.py
'''
