"""nullable_x2

Revision ID: 2bb686dcfeea
Revises: 03971bce8f1f
Create Date: 2024-05-14 12:00:28.889926

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2bb686dcfeea'
down_revision = '03971bce8f1f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('issues', schema=None) as batch_op:
        batch_op.alter_column('sequential_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('company_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('maintenance_entity_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('agreement_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('status_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('work_type_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('priority_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('created_at',
               existing_type=sa.DATETIME(),
               nullable=True)
        batch_op.alter_column('completed_at',
               existing_type=sa.DATETIME(),
               nullable=True)
        batch_op.alter_column('deadline_at',
               existing_type=sa.DATETIME(),
               nullable=True)
        batch_op.alter_column('employees_updated_at',
               existing_type=sa.DATETIME(),
               nullable=True)
        batch_op.alter_column('contacts_updated_at',
               existing_type=sa.DATETIME(),
               nullable=True)
        batch_op.alter_column('delay_to',
               existing_type=sa.DATETIME(),
               nullable=True)
        batch_op.alter_column('spent_time_total',
               existing_type=sa.FLOAT(),
               nullable=True)
        batch_op.alter_column('start_execution_until',
               existing_type=sa.DATETIME(),
               nullable=True)
        batch_op.alter_column('planned_execution_in_hours',
               existing_type=sa.FLOAT(),
               nullable=True)
        batch_op.alter_column('planned_reaction_at',
               existing_type=sa.DATETIME(),
               nullable=True)
        batch_op.alter_column('reacted_at',
               existing_type=sa.DATETIME(),
               nullable=True)
        batch_op.alter_column('deleted_at',
               existing_type=sa.DATETIME(),
               nullable=True)
        batch_op.alter_column('spent_seconds_for_reaction_in_sla',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('spent_seconds_for_completion_in_sla',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('group_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('parameters',
               existing_type=sa.TEXT(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('issues', schema=None) as batch_op:
        batch_op.alter_column('parameters',
               existing_type=sa.TEXT(),
               nullable=False)
        batch_op.alter_column('group_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('spent_seconds_for_completion_in_sla',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('spent_seconds_for_reaction_in_sla',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('deleted_at',
               existing_type=sa.DATETIME(),
               nullable=False)
        batch_op.alter_column('reacted_at',
               existing_type=sa.DATETIME(),
               nullable=False)
        batch_op.alter_column('planned_reaction_at',
               existing_type=sa.DATETIME(),
               nullable=False)
        batch_op.alter_column('planned_execution_in_hours',
               existing_type=sa.FLOAT(),
               nullable=False)
        batch_op.alter_column('start_execution_until',
               existing_type=sa.DATETIME(),
               nullable=False)
        batch_op.alter_column('spent_time_total',
               existing_type=sa.FLOAT(),
               nullable=False)
        batch_op.alter_column('delay_to',
               existing_type=sa.DATETIME(),
               nullable=False)
        batch_op.alter_column('contacts_updated_at',
               existing_type=sa.DATETIME(),
               nullable=False)
        batch_op.alter_column('employees_updated_at',
               existing_type=sa.DATETIME(),
               nullable=False)
        batch_op.alter_column('deadline_at',
               existing_type=sa.DATETIME(),
               nullable=False)
        batch_op.alter_column('completed_at',
               existing_type=sa.DATETIME(),
               nullable=False)
        batch_op.alter_column('created_at',
               existing_type=sa.DATETIME(),
               nullable=False)
        batch_op.alter_column('priority_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('work_type_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('status_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('agreement_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('maintenance_entity_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('company_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('sequential_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###