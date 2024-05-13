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
    sequential_id: Mapped[int]
    login: Mapped[str]
    email: Mapped[str]
    first_name: Mapped[str]
    last_name: Mapped[str]
    type_: Mapped[str]
    crm_1c_id: Mapped[str]
    telephony_number: Mapped[str]
    deleted_at: Mapped[datetime.datetime]
    active: Mapped[bool]
    created_at: Mapped[datetime.datetime]
    company_id: Mapped[int]  # ForeignKey("companies.id"))
    # company = relationship("Company")

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    position: Mapped[str] = mapped_column(String(300))
    patronymic: Mapped[str] = mapped_column(String(100))
    parameters: Mapped[str] = mapped_column(Text)
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
    sequential_id: Mapped[int]
    company_id: Mapped[int]  # ForeignKey("companies.id"))
    maintenance_entity_id: Mapped[int]  # ForeignKey("company_maintenance_entities.id")
    agreement_id: Mapped[int]
    status_id: Mapped[int]  # ForeignKey("issue_statuses.id"))
    work_type_id: Mapped[int]  # ForeignKey("issue_work_types.id"))
    priority_id: Mapped[int]  # ForeignKey("issue_priorities.id"))
    created_at: Mapped[datetime.datetime]
    completed_at: Mapped[datetime.datetime]
    deadline_at: Mapped[datetime.datetime]
    employees_updated_at: Mapped[datetime.datetime]
    contacts_updated_at: Mapped[datetime.datetime]
    delay_to: Mapped[datetime.datetime]
    spent_time_total: Mapped[float]
    start_execution_until: Mapped[datetime.datetime]
    planned_execution_in_hours: Mapped[float]
    planned_reaction_at: Mapped[datetime.datetime]
    reacted_at: Mapped[datetime.datetime]
    deleted_at: Mapped[datetime.datetime]
    spent_seconds_for_reaction_in_sla: Mapped[int]
    spent_seconds_for_completion_in_sla: Mapped[int]
    group_id: Mapped[int]
    contact_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=True)
    assignee_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=True)
    contact: Mapped["User"] = relationship("User", foreign_keys=[contact_id])
    assignee: Mapped["User"] = relationship("User", foreign_keys=[assignee_id])
    author: Mapped["User"] = relationship("User", foreign_keys=[author_id])

    parameters: Mapped[str] = mapped_column(Text)
    parent_id: Mapped[int]  = Column(Integer, ForeignKey("issues.id"))
    # parent_issue: Mapped = relationship("Issue", remote_side=[id])
    # company = relationship("Company")
    # maintenance_entity: Mapped  C = relationship("CompanyMaintenanceEntity")
    # status: Mapped  C = relationship("IssueStatus")
    # work_type: Mapped  C = relationship("IssueWorkType")
    # priority: Mapped  C = relationship("IssuePriority")
    # group: Mapped  C = relatinship("Group")
