from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

class User(UserMixin, db.Model):
    """
    Create a User table
    """
    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(100), nullable=False)
    lists = db.relationship("List", backref="users", lazy="dynamic", cascade="all, delete-orphan")

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.username)

# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class List(db.Model):
    """
    Create a List table
    """

    __tablename__ = 'lists'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    cards = db.relationship("Card", backref="lists", lazy="dynamic", cascade="all, delete-orphan")
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __repr__(self):
        return '<List: {}>'.format(self.name)

class Card(db.Model):
    """
    Create a Card table
    """

    __tablename__ = 'cards'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.Text)
    items = db.relationship("Item", backref="cards", lazy="dynamic", cascade="all, delete-orphan")
    list_id = db.Column(db.Integer, db.ForeignKey("lists.id"))

    def __repr__(self):
        return '<Role: {}>'.format(self.name)

class Item(db.Model):
    """
    Create a ToDo table
    """
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    date_created = db.Column(db.DateTime(), default=db.func.now())
    due_date = db.Column(db.DateTime())
    done  = db.Column(db.Boolean, nullable=False)
    card_id = db.Column(db.Integer, db.ForeignKey("cards.id"))

    def __repr__(self):
        return '<Role: {}>'.format(self.name)
