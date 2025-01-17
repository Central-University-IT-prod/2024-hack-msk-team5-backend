"""ASd

Revision ID: 7bd4a4be012f
Revises: 
Create Date: 2024-11-10 12:15:25.678253

"""

from typing import Sequence, Union

import sqlalchemy as sa
import sqlmodel
from alembic import op
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = "7bd4a4be012f"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "event",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("owner_name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column(
            "owner_description", sqlmodel.sql.sqltypes.AutoString(), nullable=True
        ),
        sa.Column("event_name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column(
            "debts",
            postgresql.ARRAY(postgresql.JSON(none_as_null=True, astext_type=sa.Text())),
            nullable=True,
        ),
        sa.Column("trip_id", sa.Uuid(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "link",
        sa.Column("value", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("type", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("allowed_user_names", postgresql.ARRAY(sa.String()), nullable=True),
        sa.PrimaryKeyConstraint("value"),
    )
    op.create_table(
        "trip",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("trip_name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("event_ids", postgresql.ARRAY(sa.UUID()), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("trip")
    op.drop_table("link")
    op.drop_table("event")
    # ### end Alembic commands ###
