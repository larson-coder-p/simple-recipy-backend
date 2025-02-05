from flask import Flask
from extensions import db
from routes import api_bp
import os

app = Flask(__name__)

# ✅ Use PostgreSQL instead of SQLite for Render
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL", "sqlite:///instance/recipe-database.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# ✅ Register API routes
app.register_blueprint(api_bp)

@app.route("/")
def home():
    return "Backend is running successfully!"

# ✅ Ensure the app runs properly on Render
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
