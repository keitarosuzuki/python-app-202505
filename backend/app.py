from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 仮のタスク一覧（リロードでリセット）
tasks = [
    {"id": 1, "text": "FlaskでAPI作成", "status": "未着手"},
    {"id": 2, "text": "Vueと接続する", "status": "未着手"},
]

@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
