from app import ma
from models import Recipe

class RecipeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Recipe

recipe_schema = RecipeSchema()
recipes_schema = RecipeSchema(many=True)
