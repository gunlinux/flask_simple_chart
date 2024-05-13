from flask import Blueprint, redirect, render_template, url_for, flash, jsonify
from chart.extensions import db
from chart.models import User
from chart.models import Issue
import sqlalchemy as sa
from sqlalchemy import func


event_blueprint = Blueprint("event", __name__)


@event_blueprint.route('/', methods=['GET'])
def index():
    return render_template('events.html')


@event_blueprint.route('/chart-data', methods=['GET'])
def chart_data():
    user_events = db.session.query(User.pagetitle, func.count(Issue.id)).join(Issue).group_by(User.id).all()

    print(user_events)
    user_names = [user[0] for user in user_events]
    event_counts = [count[1] for count in user_events]
    # Format data as JSON
    chart_data = {
        'user_names': user_names,
        'event_counts': event_counts
    }
    print(chart_data)
    return jsonify(chart_data)
