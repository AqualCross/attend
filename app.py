from flask import Flask
# from flask_migrate import Migrate
# from blueprints import login
# from blueprints import user
# from models import *
# import config


app = Flask(__name__)
# app.config.from_object(config)
# db.init_app(app)
# app.register_blueprint(user.bp)
# app.register_blueprint(login.bp)
# migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run()
