"""SqlAlchemy models."""

import datetime
from dataclasses import dataclass

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from chart.extensions import db

# from sqlalchemy.dialects.postgresql import JSONB
# events: Mapped[list["Event"]] = relationship()


@dataclass
class User(db.Model):
    __tablename__ = "users"
    sequential_id: Mapped[int] = mapped_column(nullable=True)
    login: Mapped[str] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(nullable=True)
    first_name: Mapped[str] = mapped_column(nullable=True)
    last_name: Mapped[str] = mapped_column(nullable=True)
    type_: Mapped[str] = mapped_column(nullable=True)
    crm_1c_id: Mapped[str] = mapped_column(nullable=True)
    telephony_number: Mapped[str] = mapped_column(nullable=True)
    deleted_at: Mapped[datetime.datetime] = mapped_column(nullable=True)
    active: Mapped[bool] = mapped_column(nullable=True)
    created_at: Mapped[datetime.datetime] = mapped_column(nullable=True)
    company_id: Mapped[int] = mapped_column(
        nullable=True
    )  # ForeignKey("companies.id"))

    # company = relationship("Company")

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    position: Mapped[str] = mapped_column(String(300), nullable=True)
    patronymic: Mapped[str] = mapped_column(String(100), nullable=True)
    parameters: Mapped[str] = mapped_column(Text, nullable=True)
    issues_created: Mapped[list["Issue"]] = relationship(
        "Issue", back_populates="author", foreign_keys="[Issue.author_id]"
    )
    issues_assigned: Mapped[list["Issue"]] = relationship(
        "Issue", back_populates="assignee", foreign_keys="[Issue.assignee_id]"
    )
    issues_contacted: Mapped[list["Issue"]] = relationship(
        "Issue", back_populates="contact", foreign_keys="[Issue.contact_id]"
    )


# i user can be multiple  issue
# issue can have only one,  so it's one to meny


@dataclass
class Issue(db.Model):
    __tablename__ = "issues"

    id = Column(Integer, primary_key=True)
    sequential_id: Mapped[int] = mapped_column(nullable=True)
    company_id: Mapped[int] = mapped_column(nullable=True)
    # ForeignKey("companies.id"))
    maintenance_entity_id: Mapped[int] = mapped_column(nullable=True)
    # ForeignKey("company_maintenance_entities.id")
    agreement_id: Mapped[int] = mapped_column(nullable=True)

    status_id: Mapped[int] = mapped_column(nullable=True)
    # ForeignKey("issue_statuses.id"))
    work_type_id: Mapped[int] = mapped_column(nullable=True)
    # ForeignKey("issue_work_types.id"))
    priority_id: Mapped[int] = mapped_column(nullable=True)
    # ForeignKey("issue_priorities.id"))
    created_at: Mapped[datetime.datetime] = mapped_column(nullable=True)

    completed_at: Mapped[datetime.datetime] = mapped_column(nullable=True)

    deadline_at: Mapped[datetime.datetime] = mapped_column(nullable=True)

    employees_updated_at: Mapped[datetime.datetime] = mapped_column(nullable=True)

    contacts_updated_at: Mapped[datetime.datetime] = mapped_column(nullable=True)

    delay_to: Mapped[datetime.datetime] = mapped_column(nullable=True)

    spent_time_total: Mapped[float] = mapped_column(nullable=True)

    start_execution_until: Mapped[datetime.datetime] = mapped_column(nullable=True)

    planned_execution_in_hours: Mapped[float] = mapped_column(nullable=True)

    planned_reaction_at: Mapped[datetime.datetime] = mapped_column(nullable=True)

    reacted_at: Mapped[datetime.datetime] = mapped_column(nullable=True)

    deleted_at: Mapped[datetime.datetime] = mapped_column(nullable=True)

    spent_seconds_for_reaction_in_sla: Mapped[int] = mapped_column(nullable=True)

    spent_seconds_for_completion_in_sla: Mapped[int] = mapped_column(nullable=True)

    group_id: Mapped[int] = mapped_column(nullable=True)

    contact_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=True)
    assignee_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=True)
    contact: Mapped["User"] = relationship("User", foreign_keys=[contact_id])
    assignee: Mapped["User"] = relationship("User", foreign_keys=[assignee_id])
    author: Mapped["User"] = relationship("User", foreign_keys=[author_id])

    parameters: Mapped[str] = mapped_column(Text, nullable=True)
    parent_id: Mapped[int] = mapped_column(ForeignKey("issues.id"), nullable=True)
    # parent_issue: Mapped = relationship("Issue", remote_side=[id])
    # company = relationship("Company")
    # maintenance_entity: Mapped  C = relationship("CompanyMaintenanceEntity")
    # status: Mapped  C = relationship("IssueStatus")
    # work_type: Mapped  C = relationship("IssueWorkType")
    # priority: Mapped  C = relationship("IssuePriority")
    # group: Mapped  C = relatinship("Group")
