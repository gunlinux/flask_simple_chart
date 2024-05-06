import os
import logging

from flask import Flask
from flask.cli import AppGroup

from chart.config import config
from chart.extensions import db, migrate
from chart.events.views import event_blueprint
from chart.data_generator import generate_data


logger = logging.getLogger(__name__)
user_cli = AppGroup("data")


@user_cli.command("generate")
def generate_data_cli():
    fake_users, fake_events = generate_data()
    db.session.add_all(fake_users)
    db.session.commit()

    # Generate fake events
    db.session.add_all(fake_events)
    db.session.commit()


def configure_extensions(app):
    """Configures the extensions."""
    db.init_app(app)
    migrate.init_app(app, db)


def create_app():
    app = Flask(__name__)
    env = os.environ.get("FLASK_ENV", "development")
    logger.debug("current FLASK_ENV %s", env)
    app.config.from_object(config.get(env))
    configure_extensions(app)
    app.register_blueprint(event_blueprint)
    app.cli.add_command(user_cli)
    return app
