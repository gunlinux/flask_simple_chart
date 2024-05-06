from flask import Blueprint, redirect, render_template, url_for, flash
from chart.extensions import db
import sqlalchemy as sa


event_blueprint = Blueprint("event", __name__)


@event_blueprint.route('/', methods=['GET', 'POST'])
def index():
    return 'hello here general kenobi'

