"""set the time fields

Revision ID: f7fa84c38a2a
Revises: 3b4b513527d9
Create Date: 2025-03-10 11:27:18.964467

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7fa84c38a2a'
down_revision = '3b4b513527d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('trade_booth',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('start_time', sa.Time(), nullable=False),
    sa.Column('end_time', sa.Time(), nullable=False),
    sa.Column('location', sa.String(length=255), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('image_url', sa.String(length=255), nullable=True),
    sa.Column('image_file_id', sa.String(length=255), nullable=True),
    sa.Column('document_pdf_url', sa.String(length=255), nullable=True),
    sa.Column('document_pdf_file_id', sa.String(length=255), nullable=True),
    sa.Column('document_docx_url', sa.String(length=255), nullable=True),
    sa.Column('document_docx_file_id', sa.String(length=255), nullable=True),
    sa.Column('creator_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['creator_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('trade_booth')
    # ### end Alembic commands ###
