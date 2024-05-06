"""[summary]."""

import os
import logging

from flask import Flask

from chart.config import config
from chart.extensions import db
from chart.events.views import event_blueprint


logger = logging.getLogger(__name__)


def configure_extensions(app):
    """Configures the extensions."""
    db.init_app(app)


def create_app():
    app = Flask(__name__)
    env = os.environ.get('FLASK_ENV', 'development')
    logger.debug('current FLASK_ENV %s', env)
    app.config.from_object(config.get(env))
    configure_extensions(app)
    app.register_blueprint(event_blueprint)
    return app
