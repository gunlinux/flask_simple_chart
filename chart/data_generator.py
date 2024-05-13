import random

from faker import Faker
from faker.providers import date_time

from chart.models import Issue, User


def generate_fake_users(fake, n):
    users = []
    for i in range(n):
        user = User(id=i, pagetitle=fake.name())
        users.append(user)
    return users


def generate_fake_issues(fake, users, n):
    issues = []
    print(users)
    for _ in range(n):
        user_id = random.randint(1, 10)
        issue = Issue(
            createdon=fake.date_time_between(start_date="-30d", end_date="now"),
            user_id=user_id,
        )
        issues.append(issue)
    return issues


def generate_data():
    fake = Faker()
    fake.add_provider(date_time)
    users = generate_fake_users(fake, 10)
    events = generate_fake_events(fake, users, 100)
    return users, events
