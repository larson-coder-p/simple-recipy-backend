from flask import Blueprint, request, jsonify
from extensions import db
from models import Recipe
from serializers import recipe_schema, recipes_schema

api_bp = Blueprint('api', __name__)

# Get all recipes
@api_bp.route('/recipes', methods=['GET'])
def get_recipes():
    recipes = Recipe.query.all()
    return recipes_schema.jsonify(recipes), 200

# Get a single recipe by ID
@api_bp.route('/recipes/<int:id>', methods=['GET'])
def get_recipe(id):
    recipe = Recipe.query.get(id)
    if not recipe:
        return jsonify({'error': 'Recipe not found'}), 404
    return recipe_schema.jsonify(recipe), 200

# Create a new recipe
@api_bp.route('/recipes', methods=['POST'])
def create_recipe():
    data = request.get_json()
    new_recipe = Recipe(
        title=data['title'],
        description=data['description'],
        ingredients=data['ingredients'],
        instructions=data['instructions'],
        user_id=data['user_id']  # Assume the user_id is passed in the request for now
    )
    db.session.add(new_recipe)
    db.session.commit()
    return recipe_schema.jsonify(new_recipe), 201

# Update a recipe
@api_bp.route('/recipes/<int:id>', methods=['PATCH'])
def update_recipe(id):
    recipe = Recipe.query.get(id)
    if not recipe:
        return jsonify({'error': 'Recipe not found'}), 404

    data = request.get_json()
    if 'title' in data:
        recipe.title = data['title']
    if 'description' in data:
        recipe.description = data['description']
    if 'ingredients' in data:
        recipe.ingredients = data['ingredients']
    if 'instructions' in data:
        recipe.instructions = data['instructions']

    db.session.commit()
    return recipe_schema.jsonify(recipe), 200

# Delete a recipe
@api_bp.route('/recipes/<int:id>', methods=['DELETE'])
def delete_recipe(id):
    recipe = Recipe.query.get(id)
    if not recipe:
        return jsonify({'error': 'Recipe not found'}), 404

    db.session.delete(recipe)
    db.session.commit()
    return jsonify({'message': 'Recipe deleted successfully'}), 200
