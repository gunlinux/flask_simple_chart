from faker import Faker
from faker.providers import date_time
from chart.models import User, Event


def generate_fake_users(fake, n):
    users = []
    for _ in range(n):
        user = User(pagetitle=fake.name())
        users.append(user)
    return users


def generate_fake_events(fake, users, n):
    events = []
    for _ in range(n):
        event = Event(
            createdon=fake.date_time_between(start_date="-30d", end_date="now"),
            user_id=fake.random_element(elements=[user.id for user in users]),
        )
        events.append(event)
    return events


def generate_data():
    fake = Faker()
    fake.add_provider(date_time)
    users = generate_fake_users(fake, 10)
    events = generate_fake_events(fake, users, 100)
    return users, events
