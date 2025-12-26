from flask import Flask, jsonify, send_from_directory, request
import os
import json

app = Flask(__name__, static_folder='static')

LOG_PATH = os.path.join(os.path.dirname(__file__), '..', 'logs', 'anima_exo.jsonl')

def read_last_lines(n=200):
    if not os.path.exists(LOG_PATH):
        return []
    lines = []
    with open(LOG_PATH, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except Exception:
                obj = {'raw': line}
            lines.append(obj)
    return lines[-n:]


@app.route('/')
def index():
    return send_from_directory('static', 'index.html')


@app.route('/api/logs')
def api_logs():
    n = int(request.args.get('n', '200'))
    logs = read_last_lines(n)
    return jsonify(logs)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
