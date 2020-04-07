
from quart import Quart

def create_app():
	app = Quart(__name__)

	from .user import user_api # import user_api_bp
	from .blog import blog_api # import blog_api_bp

	# 注册蓝图
	app.register_blueprint(user_api)
	app.register_blueprint(blog_api)

	return app

webapp = create_app()
