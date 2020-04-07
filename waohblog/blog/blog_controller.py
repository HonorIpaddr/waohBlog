from . import blog_api

@blog_api.route("/p/list")
async def blog_list():
	return 'list'