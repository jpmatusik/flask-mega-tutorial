from flask import Flask

from flask_mega_tutorial.config import Config


def create_app(conf_obj=Config):
    app = Flask(__name__)
    app.config.from_object(conf_obj)
    with app.app_context():
        from flask_mega_tutorial.main.routes import main_bp
        app.register_blueprint(main_bp)
        return app