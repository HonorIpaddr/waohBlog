from quart import Blueprint

user_api = Blueprint("user",__name__)

from . import user_controller

__all__=(
	'user_api',
	'user_controller'
)