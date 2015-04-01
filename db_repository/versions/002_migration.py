from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
user = Table('user', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('email', VARCHAR(length=64)),
    Column('password', VARCHAR(length=10)),
    Column('name', VARCHAR(length=64)),
)

effect = Table('effect', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('value', Integer),
    Column('token', Integer),
)

memberships = Table('memberships', post_meta,
    Column('user_id', Integer),
    Column('poll_id', Integer),
)

poll = Table('poll', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=65)),
    Column('upperbound', Integer),
    Column('lowerbound', Integer),
)

question = Table('question', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('text', String(length=250)),
)

token = Table('token', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('maximum', Integer),
    Column('minimum', Integer),
    Column('text', String(length=100)),
)

users = Table('users', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('email', String(length=64)),
    Column('password', String(length=10)),
    Column('name', String(length=64)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['user'].drop()
    post_meta.tables['effect'].create()
    post_meta.tables['memberships'].create()
    post_meta.tables['poll'].create()
    post_meta.tables['question'].create()
    post_meta.tables['token'].create()
    post_meta.tables['users'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['user'].create()
    post_meta.tables['effect'].drop()
    post_meta.tables['memberships'].drop()
    post_meta.tables['poll'].drop()
    post_meta.tables['question'].drop()
    post_meta.tables['token'].drop()
    post_meta.tables['users'].drop()
