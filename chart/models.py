"""SqlAlchemy models."""

import datetime
from dataclasses import dataclass
from chart.extensions import db
from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func


@dataclass
class User(db.Model):
    __tablename__ = "users"

    pagetitle: Mapped[str]
    id: Mapped[int] = mapped_column(primary_key=True)
    events: Mapped[list["Event"]] = relationship()


@dataclass
class Event(db.Model):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True)
    createdon: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=True)
