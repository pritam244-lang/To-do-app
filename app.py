from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

todos = []

@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)

@app.route("/todos", methods=["POST"])
def add_todo():
    data = request.json
    todos.append({"task": data["task"], "done": False})
    return jsonify({"message": "Task added!"})

@app.route("/todos/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    if 0 <= task_id < len(todos):
        todos[task_id]["done"] = True
        return jsonify({"message": "Task marked done!"})
    return jsonify({"error": "Task not found"}), 404

@app.route("/todos/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    if 0 <= task_id < len(todos):
        todos.pop(task_id)
        return jsonify({"message": "Task deleted!"})
    return jsonify({"error": "Task not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)