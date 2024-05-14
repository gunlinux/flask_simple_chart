from datetime import datetime, date, timedelta
from flask import Blueprint, render_template, request, jsonify
from chart.extensions import db
from chart.models import User
from chart.models import Issue
import sqlalchemy as sa
from sqlalchemy import func, extract


event_blueprint = Blueprint("event", __name__)


@event_blueprint.route('/', methods=['GET'])
def index():
    now = datetime.today()
    return render_template('events.html', now=now)


@event_blueprint.route('/chart-data', methods=['GET'])
def chart_data():
    # Format data as JSON
    before_q = request.args.get('before')
    after_q = request.args.get('after')
    before_date = datetime.strptime(before_q, '%d.%m.%Y')
    after_date = datetime.strptime(after_q, '%d.%m.%Y')
    after = datetime.combine(
        after_date, datetime.min.time()
    ) + timedelta(seconds=1)
    before = datetime.combine(before_date, datetime.min.time())
    print(after, before)
    events = (
        db.session.query(
            func.count(Issue.id),
            extract("hour", Issue.created_at).label("hour"),
        )
        .filter(Issue.created_at.between(after, before))
        .group_by(extract("hour", Issue.created_at))
        .all()
    )
    hourly_events_dict = {hour: count for count, hour in events}
    chart_data = {
        'event_counts': [hourly_events_dict.get(x, 0) for x in range(0, 24)],
        'hours': [x for x in range(0, 24)],
    }
    return jsonify(chart_data)
