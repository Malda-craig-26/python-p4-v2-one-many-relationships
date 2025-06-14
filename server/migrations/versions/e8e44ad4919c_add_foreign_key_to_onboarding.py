"""add foreign key to onboarding

Revision ID: e8e44ad4919c
Revises: ecbcec74d7d1
Create Date: 2025-06-14 04:12:52.145169

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8e44ad4919c'
down_revision = 'ecbcec74d7d1'
branch_labels = None
depends_on = None


def upgrade():
    # Use batch mode for tables in SQLite
    with op.batch_alter_table('onboardings') as batch_op:
        batch_op.add_column(sa.Column('employee_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_onboardings_employee_id_employees', 'employees', ['employee_id'], ['id'])
    # For the 'reviews' table, if you're adding a foreign key or schema change, also do it in batch mode
    with op.batch_alter_table('reviews') as batch_op:
        batch_op.create_foreign_key('fk_reviews_employee_id_employees', 'employees', ['employee_id'], ['id'])

def downgrade():
    # Drop foreign keys in reverse order, also in batch mode
    with op.batch_alter_table('reviews') as batch_op:
        batch_op.drop_constraint('fk_reviews_employee_id_employees', type_='foreignkey')
    with op.batch_alter_table('onboardings') as batch_op:
        batch_op.drop_constraint('fk_onboardings_employee_id_employees', type_='foreignkey')
        batch_op.drop_column('employee_id')