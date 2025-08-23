"""description added for books table

Revision ID: 286fbef4be11
Revises: 5675b6bff18d
Create Date: 2025-08-22 18:48:05.171768

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '286fbef4be11'
down_revision: Union[str, None] = '5675b6bff18d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(length=250), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.drop_column('description')
    # ### end Alembic commands ###
