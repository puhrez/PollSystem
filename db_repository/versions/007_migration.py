from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
tokens = Table('tokens', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('poll_id', Integer),
    Column('maximum', Integer),
    Column('minimum', Integer),
    Column('text', String(length=100)),
)

effects = Table('effects', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('value', Integer),
    Column('question_id', Integer),
    Column('token', Integer),
)

questions = Table('questions', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('text', String(length=250)),
    Column('poll_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['tokens'].columns['poll_id'].create()
    post_meta.tables['effects'].columns['question_id'].create()
    post_meta.tables['questions'].columns['poll_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['tokens'].columns['poll_id'].drop()
    post_meta.tables['effects'].columns['question_id'].drop()
    post_meta.tables['questions'].columns['poll_id'].drop()
