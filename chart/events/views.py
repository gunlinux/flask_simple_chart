from flask import Blueprint, redirect, render_template, url_for, flash, jsonify
from chart.extensions import db
import sqlalchemy as sa


event_blueprint = Blueprint("event", __name__)


@event_blueprint.route('/', methods=['GET'])
def index():
    return render_template('events.html')


@event_blueprint.route('/chart-data', methods=['GET'])
def chart_data():
    chart_data = {
        'user_names': [f'user{id}' for id in range(1, 5)],
        'event_counts': list(range(1, 5)),
    }
    return jsonify(chart_data)
