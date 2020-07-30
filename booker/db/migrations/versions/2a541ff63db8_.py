"""empty message

Revision ID: 2a541ff63db8
Revises:
Create Date: 2020-07-28 08:52:10.016578

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = "2a541ff63db8"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "txs",
        sa.Column("id", sqlalchemy_utils.types.uuid.UUIDType(), nullable=False),
        sa.Column("coin", sa.String(), nullable=False),
        sa.Column("tx_id", sa.String(), nullable=True),
        sa.Column("from_address", sa.String(), nullable=True),
        sa.Column("to_address", sa.String(), nullable=True),
        sa.Column(
            "amount",
            sa.Numeric(precision=78, scale=36),
            server_default="0.0",
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column(
            "error",
            sa.Enum("NO_ERROR", "UNKNOWN_ERROR", name="txerror"),
            server_default="NO_ERROR",
            nullable=False,
        ),
        sa.Column("confirmations", sa.Integer(), server_default="0", nullable=False),
        sa.Column(
            "max_confirmations", sa.Integer(), server_default="0", nullable=False
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("coin", "tx_id"),
    )
    op.create_table(
        "orders",
        sa.Column("id", sqlalchemy_utils.types.uuid.UUIDType(), nullable=False),
        sa.Column(
            "type",
            sa.Enum("TRASH", "DEPOSIT", "WITHDRAWAL", name="ordertype"),
            server_default="TRASH",
            nullable=False,
        ),
        sa.Column(
            "party",
            sa.Enum("INIT", "IN_CREATED", "OUT_CREATED", name="gatewayparty"),
            server_default="INIT",
            nullable=False,
        ),
        sa.Column("in_tx", sqlalchemy_utils.types.uuid.UUIDType(), nullable=False),
        sa.Column("out_tx", sqlalchemy_utils.types.uuid.UUIDType(), nullable=False),
        sa.ForeignKeyConstraint(["in_tx"], ["txs.id"]),
        sa.ForeignKeyConstraint(["out_tx"], ["txs.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("orders")
    op.drop_table("txs")
    # ### end Alembic commands ###
