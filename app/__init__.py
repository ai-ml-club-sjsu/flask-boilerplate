from flask import Flask
from .config import Config
from .extensions import init_extensions
from .routes import bp as main_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    init_extensions(app)
    app.register_blueprint(main_bp)

    return app
