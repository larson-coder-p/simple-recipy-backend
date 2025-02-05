from extensions import db
from flask_bcrypt import generate_password_hash

# Association table for Recipe-Category Many-to-Many relationship
recipe_category = db.Table('recipe_category',
    db.Column('recipe_id', db.Integer, db.ForeignKey('recipes.id')),
    db.Column('category_id', db.Integer, db.ForeignKey('categories.id'))
)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password).decode('utf8')

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

    # Relationships
    user = db.relationship('User', backref=db.backref('recipes', lazy=True))
    categories = db.relationship('Category', secondary=recipe_category, backref=db.backref('recipes', lazy=True))

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
