from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
tokens = Table('tokens', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('poll_id', Integer),
    Column('is_upperbound', Boolean),
    Column('is_lowerbound', Boolean),
    Column('maximum', Integer),
    Column('minimum', Integer),
    Column('text', String(length=100)),
)

polls = Table('polls', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=65)),
    Column('timestamp', DateTime),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['tokens'].columns['is_upperbound'].create()
    post_meta.tables['polls'].columns['timestamp'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['tokens'].columns['is_upperbound'].drop()
    post_meta.tables['polls'].columns['timestamp'].drop()
