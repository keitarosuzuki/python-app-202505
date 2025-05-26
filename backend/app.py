from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import os, requests, json

load_dotenv()

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
  
@app.route("/api/tasks", methods=["POST"])
def add_task():
    data = request.json
    new_task = {
        "id": len(tasks) + 1,
        "text": data["text"],
        "status": "未着手"
    }
    tasks.append(new_task)
    return jsonify(new_task), 201
  
@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return jsonify({"message": f"タスク {task_id} を削除しました"}), 200
  
@app.route("/api/generate-tasks", methods=["POST"])
def generate_tasks():
    data = request.json
    user_input = data.get("text", "")

    prompt = f"""
    以下のやりたいことを、5つの具体的な作業タスクに日本語で分解してください。

    やりたいこと:
    {user_input}

    出力形式（JSON）:
    [
        {{ "text": "◯◯を作る", "status": "未着手" }},
        ...
    ]
    """

    headers = {
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json",
    }

    body = {
        "model": "openai/gpt-3.5-turbo",  # または他の無料モデル
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=body)

    if response.ok:
        try:
            message = response.json()["choices"][0]["message"]["content"]
            tasks = json.loads(message)
            return jsonify(tasks), 200
        except Exception as e:
            return jsonify({"error": "出力形式が正しくありません"}), 500
    else:
        return jsonify({"error": response.text}), response.status_code

if __name__ == "__main__":
    app.run(debug=True, port=5000)
