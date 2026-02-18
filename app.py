import os
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf import CSRFProtect
from translations import TRANSLATIONS, SUPPORTED_LANGUAGES, DEFAULT_LANGUAGE

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()


def get_lang():
    return session.get("lang", DEFAULT_LANGUAGE)


def t(key, **kwargs):
    lang = get_lang()
    text = TRANSLATIONS.get(lang, {}).get(key)
    if text is None:
        text = TRANSLATIONS[DEFAULT_LANGUAGE].get(key, key)
    if kwargs:
        text = text.format(**kwargs)
    return text


def create_app():
    app = Flask(__name__)

    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret-change-in-production")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "income_tracker.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    login_manager.login_view = "auth.login"
    login_manager.login_message = "flash_login_required"
    login_manager.login_message_category = "info"
    login_manager.localize_callback = t

    @app.context_processor
    def inject_translation_helpers():
        return {
            "t": t,
            "current_lang": get_lang(),
            "supported_languages": SUPPORTED_LANGUAGES,
        }

    from models import User

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

    from routes.auth import auth_bp
    from routes.main import main_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    with app.app_context():
        db.create_all()

    return app
