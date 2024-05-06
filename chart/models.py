"""SqlAlchemy models."""
import datetime
from chart.extensions import db
from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func


class User(db.Model):
    """orm model for blog post."""

    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    pagetitle: Mapped[str]


class Event(db.Model):
    """orm model for blog post."""

    __tablename__ = 'events'
    id: Mapped[int] = mapped_column(primary_key=True)
    createdon: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=True)
    user: Mapped["User"] = relationship(back_populates="events")
