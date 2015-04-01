from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
effect = Table('effect', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('value', INTEGER),
    Column('token', INTEGER),
)

poll = Table('poll', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=65)),
    Column('upperbound', INTEGER),
    Column('lowerbound', INTEGER),
)

question = Table('question', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('text', VARCHAR(length=250)),
)

token = Table('token', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('maximum', INTEGER),
    Column('minimum', INTEGER),
    Column('text', VARCHAR(length=100)),
)

effects = Table('effects', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('value', Integer),
    Column('token', Integer),
)

polls = Table('polls', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=65)),
    Column('upperbound', Integer),
    Column('lowerbound', Integer),
)

questions = Table('questions', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('text', String(length=250)),
)

tokens = Table('tokens', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('maximum', Integer),
    Column('minimum', Integer),
    Column('text', String(length=100)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['effect'].drop()
    pre_meta.tables['poll'].drop()
    pre_meta.tables['question'].drop()
    pre_meta.tables['token'].drop()
    post_meta.tables['effects'].create()
    post_meta.tables['polls'].create()
    post_meta.tables['questions'].create()
    post_meta.tables['tokens'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['effect'].create()
    pre_meta.tables['poll'].create()
    pre_meta.tables['question'].create()
    pre_meta.tables['token'].create()
    post_meta.tables['effects'].drop()
    post_meta.tables['polls'].drop()
    post_meta.tables['questions'].drop()
    post_meta.tables['tokens'].drop()
