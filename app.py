from flask import Flask, jsonify
from flask_migrate import Migrate  # ✅ Import Flask-Migrate
from extensions import db
from routes import api_bp
import os

app = Flask(__name__)

# ✅ Use PostgreSQL in production
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL", "sqlite:///instance/recipe-database.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)  # ✅ Initialize Flask-Migrate

# ✅ Register Blueprint only ONCE
if not hasattr(app, "api_registered"):
    app.register_blueprint(api_bp)
    app.api_registered = True

@app.route("/")
def home():
    return "Backend is running successfully!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
