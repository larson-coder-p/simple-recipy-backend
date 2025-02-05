from flask import Blueprint, jsonify
from extensions import db
from models import Recipe

api_bp = Blueprint("api", __name__, url_prefix="/api")  # ✅ Add a `url_prefix`

@api_bp.route("/recipes", methods=["GET"])
def list_recipes():  # ✅ Change function name to avoid conflicts
    recipes = Recipe.query.all()
    return jsonify([recipe.to_dict() for recipe in recipes])

@api_bp.route("/recipes/<int:id>", methods=["GET"])
def get_recipe(id):
    recipe = Recipe.query.get_or_404(id)
    return jsonify(recipe.to_dict())
