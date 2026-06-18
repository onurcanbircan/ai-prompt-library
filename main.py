import os
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Veritabanı yapılandırması (SQLite)
db_path = os.path.join(os.path.dirname(__file__), 'prompts.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Veritabanı veri modeli tanımlaması
class Prompt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), default="")
    prompt_text = db.Column(db.Text, nullable=False)
    usage_count = db.Column(db.Integer, default=0)

    def to_dict(self):
        """Veritabanı nesnesini JSON formatına uygun sözlük yapısına dönüştürür."""
        return {
            "id": self.id,
            "title": self.title,
            "category": self.category,
            "description": self.description,
            "prompt_text": self.prompt_text,
            "usage_count": self.usage_count
        }

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/prompts", methods=["POST"])
def add_prompt():
    data = request.json
    # Zorunlu alanların varlık ve doluluk kontrolü
    if not data or not data.get("title") or not data.get("prompt_text") or not data.get("category"):
        return jsonify({"error": "title, prompt_text ve category boş olamaz"}), 400
    
    new_prompt = Prompt(
        title=data["title"],
        category=data["category"],
        description=data.get("description", ""),
        prompt_text=data["prompt_text"]
    )
    
    db.session.add(new_prompt)
    db.session.commit()
    return jsonify(new_prompt.to_dict()), 201

@app.route("/api/prompts", methods=["GET"])
def list_prompts():
    # Kayıtları azalan sırada (en yeni kayıt en üstte olacak şekilde) listeler
    prompts = Prompt.query.order_by(Prompt.id.desc()).all()
    return jsonify([p.to_dict() for p in prompts])

@app.route("/api/prompts/<int:prompt_id>", methods=["GET"])
def get_prompt(prompt_id):
    prompt = Prompt.query.get(prompt_id)
    if prompt:
        return jsonify(prompt.to_dict())
    return jsonify({"error": "Prompt not found"}), 404

@app.route("/api/prompts/<int:prompt_id>/use", methods=["POST"])
def use_prompt(prompt_id):
    # İlgili promptun kullanım istatistiğini bir artırır ve güncel veriyi döner
    prompt = Prompt.query.get(prompt_id)
    if prompt:
        prompt.usage_count += 1
        db.session.commit()
        return jsonify(prompt.to_dict())
    return jsonify({"error": "Prompt not found"}), 404

@app.route("/api/prompts/<int:prompt_id>", methods=["DELETE"])
def delete_prompt(prompt_id):
    prompt = Prompt.query.get(prompt_id)
    if prompt:
        db.session.delete(prompt)
        db.session.commit()
        return jsonify({"message": "Prompt başarıyla silindi"}), 200
    return jsonify({"error": "Prompt not found"}), 404

if __name__ == "__main__":
    # Uygulama ayağa kalkmadan önce veritabanı şemasını ve tabloları otomatik olarak oluşturur
    with app.app_context():
        db.create_all()
    app.run(debug=True)