from quart import Blueprint

blog_api = Blueprint("blog",__name__)

from . import blog_controller