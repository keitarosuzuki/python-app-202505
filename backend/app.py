from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import os, requests, json

load_dotenv()

app = Flask(__name__)
CORS(app)
  
@app.route("/api/generate-tasks", methods=["POST"])
def generate_tasks():
    data = request.json
    user_input_text = data.get("text", "")
    user_input_count = data.get("count", "")

    prompt = f"""
    以下のやりたいことを、指定された件数の具体的な作業タスクに日本語で分解してください。

    やりたいこと:
    {user_input_text}

    件数:
    {user_input_count}

    出力形式（JSON）:
    [
        {{ "id": 1, "text": "◯◯を作る" }},
        ...
    ]
    """

    headers = {
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json",
    }

    body = {
        "model": "openai/gpt-3.5-turbo",
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
