from blogApp import app
app=app.create_app()
# 如果希望直接terminal启动，反注释下面两行，python dev.py
# if __name__ == '__main__':
# 	app.run(host="localhost",port=5000,debug=True)