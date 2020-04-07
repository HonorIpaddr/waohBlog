from . import user_api


@user_api.route("/login")
async def login():
	return "login api"

@user_api.route("/logout")
async def logout():
	return "logout api"
