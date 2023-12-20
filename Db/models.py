from . import db
from flask_login import UserMixin

#Таблица пользователи 
class users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(102), nullable=False)
    admin_on_off = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"id:{self.id}, username:{self.username}, admin_on_off:{self.admin_on_off}"

#Таблица рецепты
class recipes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_dish = db.Column(db.String(100), nullable=False)
    photo_link = db.Column(db.String, nullable=True)
    ingridients = db.Column(db.String, nullable=False)
    steps = db.Column(db.String, nullable=False)
    
    def __repr__(self):
        return f"id:{self.id}, name_dish:{self.name_dish}, photo_link:{self.photo_link}, ingridients:{self.ingridients}, steps:{self.steps}"
