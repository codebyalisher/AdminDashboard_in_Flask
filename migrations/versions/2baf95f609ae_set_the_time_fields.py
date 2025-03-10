"""set the time fields

Revision ID: 2baf95f609ae
Revises: a3a6fbd2946f
Create Date: 2025-03-10 11:44:57.195750

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2baf95f609ae'
down_revision = 'a3a6fbd2946f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('trade_booth', schema=None) as batch_op:
        batch_op.drop_column('image_filename')
        batch_op.drop_column('document_docx_filename')
        batch_op.drop_column('document_pdf_filename')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('trade_booth', schema=None) as batch_op:
        batch_op.add_column(sa.Column('document_pdf_filename', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('document_docx_filename', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('image_filename', sa.VARCHAR(length=255), autoincrement=False, nullable=True))

    # ### end Alembic commands ###
