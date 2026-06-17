from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

prompts = []
next_id = 1

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/prompts", methods=["POST"])
def add_prompt():
    global next_id
    data = request.json
    if not data.get("title") or not data.get("prompt_text") or not data.get("category"):
        return jsonify({"error": "title, prompt_text ve category boş olamaz"}), 400
    
    prompt = {
        "id": next_id,
        "title": data["title"],
        "description": data.get("description", ""),
        "prompt_text": data["prompt_text"],
        "category": data["category"],
        "usage_count": 0
    }
    prompts.append(prompt)
    next_id += 1
    return jsonify(prompt), 201

@app.route("/api/prompts", methods=["GET"])
def list_prompts():
    return jsonify(prompts)

@app.route("/api/prompts/<int:prompt_id>", methods=["GET"])
def get_prompt(prompt_id):
    for p in prompts:
        if p["id"] == prompt_id:
            return jsonify(p)
    return jsonify({"error": "Prompt not found"}), 404

@app.route("/api/prompts/<int:prompt_id>/use", methods=["GET"])
def use_prompt(prompt_id):
    for p in prompts:
        if p["id"] == prompt_id:
            p["usage_count"] += 1
            return jsonify(p)
    return jsonify({"error": "Prompt not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)