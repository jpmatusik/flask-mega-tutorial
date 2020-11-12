from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

from flask_mega_tutorial.config import Config

bcrypt = Bcrypt()
db = SQLAlchemy(metadata=MetaData(naming_convention={
  "ix": "ix_%(column_0_label)s",
  "uq": "uq_%(table_name)s_%(column_0_name)s",
  "ck": "ck_%(table_name)s_%(constraint_name)s",
  "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
  "pk": "pk_%(table_name)s"
}))
login_manager = LoginManager()
login_manager.login_view = 'users_bp.login'
login_manager.login_message_category = 'warn'
migrate = Migrate()


def create_app(conf_obj=Config):
    app = Flask(__name__)
    app.config.from_object(conf_obj)
    app.jinja_options.update(conf_obj.JINJA_OPTIONS)
    with app.app_context():
        bcrypt.init_app(app)
        db.init_app(app)
        login_manager.init_app(app)
        migrate.init_app(app, db)

        from flask_mega_tutorial.main.routes import main_bp
        from flask_mega_tutorial.posts.routes import posts_bp
        from flask_mega_tutorial.users.routes import users_bp
        app.register_blueprint(main_bp)
        app.register_blueprint(users_bp)
        app.register_blueprint(posts_bp)

        return app
