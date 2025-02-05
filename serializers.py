from extensions import ma  # ✅ Import ma from extensions
from models import Recipe

class RecipeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Recipe
        load_instance = True

recipe_schema = RecipeSchema()
recipes_schema = RecipeSchema(many=True)
