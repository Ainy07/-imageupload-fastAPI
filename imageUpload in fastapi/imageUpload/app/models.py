from fastapi import FastAPI
from tortoise.models import Model
from datetime import datetime
from tortoise import Tortoise, fields


class Category(Model):
    name = fields.CharField(200, unique=True)
    slag = fields.CharField(200)
    category_image = fields.TextField()
    discription = fields.TextField()
    is_active = fields.BooleanField(default=True)
    updated_at = fields.DatetimeField(auto_now=True)
    created_at = fields.DatetimeField(auto_now_add=True)






Tortoise.init_models(['app.models'], 'models')
