from faker import Faker
from faker.providers import date_time
from chart.models import User, Event
import random


def generate_fake_users(fake, n):
    users = []
    for i in range(n):
        user = User(id=i, pagetitle=fake.name())
        users.append(user)
    return users


def generate_fake_events(fake, users, n):
    events = []
    print(users)
    for _ in range(n):
        user_id = random.randint(1, 10)
        event = Event(
            createdon=fake.date_time_between(start_date="-30d", end_date="now"),
            user_id=user_id,
        )
        events.append(event)
    return events


def generate_data():
    fake = Faker()
    fake.add_provider(date_time)
    users = generate_fake_users(fake, 10)
    events = generate_fake_events(fake, users, 3000)
    return users, events
