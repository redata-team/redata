"""Add scan

Revision ID: 184924ecd052
Revises: 8be0b8538d61
Create Date: 2021-03-07 16:15:30.259925

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "184924ecd052"
down_revision = "8be0b8538d61"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "scan",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(), nullable=True),
        sa.Column("start_date", sa.TIMESTAMP(), nullable=True),
        sa.Column("end_date", sa.TIMESTAMP(), nullable=True),
        sa.Column("status", sa.String(), nullable=True),
        sa.Column("run_type", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.drop_table("run")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "run",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
        sa.Column(
            "for_date", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
        sa.Column("status", sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column("run_type", sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.PrimaryKeyConstraint("id", name="run_pkey"),
    )
    op.drop_table("scan")
    # ### end Alembic commands ###
