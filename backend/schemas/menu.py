from tortoise.contrib.pydantic import pydantic_model_creator

from models import MenuModel

MenuRead = pydantic_model_creator(MenuModel, name="MenuOut")
MenuIn = pydantic_model_creator(MenuModel, name="MenuIn", exclude_readonly=True)
